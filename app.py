from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        feedback = request.form['feedback']
        # Process the feedback (you can save it to a database or perform other actions)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
