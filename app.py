from flask import Flask, render_template, request, jsonify, redirect, url_for, Blueprint, session
import json
import numpy as np
import random
import datetime
from config.experiment import *

# Initialize the Flask application
app = Flask(__name__)  
app.secret_key = 'this_is_a_random_key'

# Create blueprints for static folders
styles_bp = Blueprint('styles', __name__, static_folder='styles', static_url_path='/styles')
data_bp = Blueprint('data', __name__, static_folder='data', static_url_path='/data')

# Register blueprints with the Flask application
app.register_blueprint(styles_bp)
app.register_blueprint(data_bp)

START = None

def sessionPlanner():
    """
    Create a session based on the experiment parameters defined in /config/experiment.py

    Check the /config/experiment.py for a detailed explanation of the experiment structure
    """
    if len(session['SESSION']) == 0:
        # Create a list of the Experiment Parts
        len_exp = len(EXPERIMENT) - 1
        order = list(range(len_exp))
        # Randomize the order of the Parts
        if EXPERIMENT['Config']['Random_part']:
            random.shuffle(order)
        for j, n_order in enumerate(order):
            # Get Part
            part = list(EXPERIMENT.keys())[n_order+1]
            # Get (test) Pages
            tests = EXPERIMENT[part]
            # Randomize the order of the Pages
            if EXPERIMENT['Config']['Random_page']:
                random.shuffle(tests)
            # For each Page
            for test in tests:
                stimulus = len(test) - 1
                stimulus_order = list(range(stimulus))
                # Randomize the order of the Stimulus
                if test['Config']['Random']:
                    random.shuffle(stimulus_order)
                stimulus = [ [list(test.keys())[n_stimulys+1], list(test.values())[n_stimulys+1] ] for n_stimulys in stimulus_order]
                # Add to session
                # 'SESSION' is the list of pages to be presented
                session['SESSION'].append([
                    'Page'+str(len(session['SESSION'])+1),
                    part,
                    test['Config']['Name'],
                    test['Config']['Mode'],
                    stimulus
                ])

def printSession():
    """
    Print pages to be presented in the session in order
    """
    for page in session['SESSION']:
        print(page[0])
        print(page[1], page[2], page[3])
        for stimulus in page[4]:
            print(stimulus[0])
            print(stimulus[1])
        print('---------')

def getNextPage():
    """
    Delete the current page from the session and return the next page
    """
    if len(session['SESSION']) > 0:
        session['RECORDED'].append(session['SESSION'].pop(0))
        session.modified = True
        return session['RECORDED'][-1]
    else:
        return None

def checkNextPage():
    """
    This does not register the page, just checks the next page
    """
    if len(session['SESSION']) > 0:
        return session['SESSION'][0]

def getCurrentPage():
    """
    Get the current page of the session
    """
    if len(session['RECORDED']) > 0:
        return session['RECORDED'][-1]
    return None
    
def page2dict(page):
    """
    Convert page to dictionary to be used in the HTML templates.
    This info is sent to javascript to render the page.
    """
    if page:
        page_number = len([p for p in session['RECORDED'] if p[1] == page[1]])
        return dict(
                {
                'Page ID'    : page[0], # Number of the page in the experiment
                'Part'       : page[1], # Part of the experiment
                'Test'       : page[2], # Page name
                'Mode'       : page[3], # Type (mode) of page
                'VSource'    : EXPERIMENT['Config']['VideoSource'], # Source of the videos (local or youtube)
                'VConfig'    : VIDEO_PARAMS, # Video parameters such as controls, autoplay, etc
                'PageNumber' : page_number, # Number of the Page in the Part
                'PageTotal'  : len(EXPERIMENT[page[1]]), # Total number of Pages in the Part
                }, 
                # Create a dictionary for each stimulus in the page
                # The first dict is the stimulus number and its name
                **{'S'+str(i+1)  : stimulus[0]  for i, stimulus in enumerate(page[4])},
                # The second dict is the stimulus' URL
                **{'URL'+str(i+1): stimulus[1]  for i, stimulus in enumerate(page[4])},
            )
    else:
        return None

def registerAnswer(answer):
    """
    Register the answer of a given Page.

    The answer can be processed differently depending on the type (mode) of the Page.
    After the answer is processed, it is added to the session['ANSWERS'] list.
    Once the session is finished, the answers are saved *AS IS* to a file.
    Therefore, the processing of the answers should be done in this function.
    """
    # Get what is registered in the current page
    print('REGISTERING ANSWER')
    page = page2dict(getCurrentPage())
    #print(page)
    if page['Mode'] == 'MUSHRA':                                            # Registration for MUSHRA type of page
        part = EXPERIMENT[page['Part']]                                     # Get the part of the experiment
        for test in part:                                                   # Run through the tests of the part
            if test['Config']['Name'] == page['Test']:                      # Checks which test is the current page
                session['ANSWERS'].append( [ [page['Mode'], page['Part'], page['Test'], page['S'+str(i+1)] , score[1] ] for i, score in enumerate(answer.items())] ) # Add the answer to the session
                #for i, score in enumerate(answer.items()):                  # Run through the answers (in the order presented to the user)
                #    test.update({page['S'+str(i+1)]+'_Score' : score[1]})   # Get the stimulus corresponding to the answer and register the score
                break                                                       # Since the test was found, there is no need to continue the loop
    
    elif page['Mode'] == 'AB':                                              # Registration for AB type of page
        part = EXPERIMENT[page['Part']]                                     # Get the part of the experiment
        for test in part:                                                   # Run through the tests of the part
            if test['Config']['Name'] == page['Test']:                      # Checks which test is the current page
                session['ANSWERS'].append([page['Mode'], page['Part'], page['Test'], page['S1'], page['S2'], answer] )
                break

    elif page['Mode'] == 'Single' or page['Mode'] == 'Single_v2':                                              # Registration for AB type of page
        part = EXPERIMENT[page['Part']]                                     # Get the part of the experiment
        for test in part:                                                   # Run through the tests of the part
            if test['Config']['Name'] == page['Test']:                      # Checks which test is the current page
                session['ANSWERS'].append([page['Mode'], page['Part'], page['Test'], page['S1'], answer] )
                break
    session['ANSWERS'][-1].append(datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S"))
    session.modified = True
    logSession()
    printAnswers()

def logSession():
    """
    Save a log with the current answers of the session.
    This is useful to recover the session in case of a crash.
    """
    with open('sessionlogs/' + session['id'] + '.json', 'w') as outfile:
        json.dump(session, outfile, indent=4)

@app.route('/loadSession', methods=['GET', 'POST'])
def loadSession():
    """
    Recover a session from a log file.
    This function can only be called through index.html
    """
    try:
        data = request.get_json()
        assert data is not None, 'No data provided'
        # Load log data
        with open('sessionlogs/' + data['id'] + '.json') as file:
            session_data = json.load(file)
        # Update session
        session.update(session_data)
        # redirect to the next page
        return process_answer()
    except Exception as e:
        print('error on loadSession: ', e)
        return jsonify({'error on process_answer': str(e)})


def printAnswers():
    """
    Print every answer in the session
    """
    for entry in session['ANSWERS']:
        print(entry)
            
def saveResults():
    """
    Save the results. Called when the session is finished.
    """
    printAnswers()
    # Save the results to a file
    end = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    file = "./results/"+session['id']+".csv"
    with open(file, 'w') as f:
        f.write(str(START))
        f.write(',')
        f.write(str(end))
        f.write('\n')
        for entry in session['ANSWERS']:
            for cell in entry:
                f.write(str(cell))
                f.write(',')
            f.write('\n')

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Start a new session. This is the first page of the experiment.
    It is called when the user access the website or every time the user enters the URL and updates the page.
    """
    print('-----------------------------------------------------------')
    print('----------------------- NEW SESSION -----------------------')
    print('-----------------------------------------------------------')
    # Creates a new and unique session using Flask's session
    # This prevents that different users interfere with each other
    session['id'] = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    session['SESSION'] = []
    session['RECORDED'] = []
    session['ANSWERS'] = []
    #printClientSession()
    return render_template("index.html", data={'id': session['id']})

@app.route('/process_answer', methods=['POST'])
def process_answer():
    """
    One of the most important functions of the experiment.
    It processes the answer of the user and redirects to the next page.
    """
    try:
        # Get the data sent by the client
        data = request.get_json()
        assert data is not None, 'No data provided'

        # Should only enter here after the index.html Page
        if 'Next' in data:
            if data['Next'] == "introp1":
                return jsonify({'redirect': '\introp1'})
            else:
                print("Something went wrong")
                
        # The Page before the experiment starts should enter here
        # i.e., if your experiment have lots of pages before the actual experiment starts
        # only the last one should send "{'Start': true}" back to Flask
        elif 'Start' in data:
            if len(session['SESSION']) == 0:
                sessionPlanner()
                global START
                START = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
            return loadNextPage()
        
        # The actual experiment should enter here. Every Page in the experiment should pass through this code
        elif 'NextPage' in data:

            # Register the answer given the data sent by the client
            # The data sent by the client is different for each type of page
            # There is no need to handle this difference here since it is handled in the registerAnswer function
            # so this should be corrected in the future
            currentPage = page2dict(getCurrentPage())
            if 'videoScores' in data: # If it is a MUSHRA page
                registerAnswer(data['videoScores'])
            elif 'selectedValue' in data: # If it is a AB page
                registerAnswer(data['selectedValue'])

            # Checks the current and the next Page, if they have different modes (types), 
            # redirect to the intro page of the next mode. 
            # They are not part of the experiment, i.e., they are not listed in the session, that's why they are handled differently
            # Remove it if you don't have intro pages for each mode or different modes
            currentPage = page2dict(getCurrentPage())
            nextPage = page2dict(checkNextPage())
            if nextPage:
                if nextPage['Mode'] != currentPage['Mode']:
                    if nextPage['Mode'] == 'AB':
                        return jsonify({'redirect': '\introp2'})
                    elif nextPage['Mode'] == 'Single_v2':
                        return jsonify({'redirect': '\introp3'})
                    elif nextPage['Mode'] == 'Single':
                        return jsonify({'redirect': '\introp4'})
                    else:
                        print('Error on process_answer: no intro for the next page mode.')

            # If there is no next Page, save the results and redirect to the end page
            elif not nextPage:
                print('You have reached the end of the experiment. Saving results.')
                saveResults()
                return jsonify({'redirect': url_for('end')})

            # Change to the next page. This should be the last thing to do
            return loadNextPage()
        
        # The intro pages are not part of the experiment. They are just to introduce the next mode (type) of the experiment
        # After these pages, get back to the experiment
        elif 'outIntro' in data:
            return loadNextPage()
                
    # Catch any error and return it to the client
    except Exception as e:
        print('Caught an error on process_answer: ', e)
        return jsonify({'error on process_answer': str(e)})
    
def getURL(page):
    """
    Get the correct URL for any page
    """
    if page == 'MUSHRA':
        return jsonify({'redirect': url_for('MUSHRA')})
    elif page == 'AB':
        return jsonify({'redirect': url_for('AB')})
    elif page == 'Single':
        return jsonify({'redirect': url_for('SINGLE')})
    elif page == 'Single_v2':
        return jsonify({'redirect': url_for('SINGLE_v2')})

def loadNextPage():
    """
    Delete the current page from the session and get the next page from getNextPage()
    Returns the URL of the next page
    """
    page = page2dict(getNextPage())
    if page:
        return getURL(page['Mode'])
    else: 
        print('No next page found')
        return None

@app.route('/message')
def message():
    return render_template('message.html')

@app.route('/mushra')
def MUSHRA():
    pagedict = page2dict(getCurrentPage())
    return render_template('MUSHRA.html', data=pagedict)

@app.route('/ab')
def AB():
    pagedict = page2dict(getCurrentPage())
    return render_template('AB.html', data=pagedict)

@app.route('/single')
def SINGLE():
    pagedict = page2dict(getCurrentPage())
    return render_template('Single.html', data=pagedict)

@app.route('/single_v2')
def SINGLE_v2():
    pagedict = page2dict(getCurrentPage())
    return render_template('Single_v2.html', data=pagedict)

@app.route('/finished')
def end():
    return render_template('end.html')

@app.route('/introp1')
def introp1():
    return render_template('introp1.html')

@app.route('/introp2')
def introp2():
    return render_template('introp2.html')

@app.route('/introp3')
def introp3():
    return render_template('introp3.html')

@app.route('/introp4')
def introp4():
    return render_template('introp4.html')

def printClientSession(full=True):
    """
    Print the current session of the client
    """
    print('-----------------------------')
    print('-------CLIENT SESSION--------')
    print('-----------------------------')
    print('ID: ', session['id'])
    print('SESSION: ', len(session['SESSION']))
    print('RECORDED: ', len(session['RECORDED']))
    print('ANSWERS: ', len(session['ANSWERS']))
    if full:
        printAnswers()
    
# Run the app
# Some servers require that you delete this if statement    
if __name__ == '__main__':
    app.run(debug=True)
