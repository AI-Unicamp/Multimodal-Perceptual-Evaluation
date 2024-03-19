# Description: Configuration file for the experiment. It contains the experiment structure and the video sources.
# Terms used:
# Experiment    - The entire experiment, which is composed of parts. 
#                 One participant will go through everuthing contained in the experiment.
#                 A "session" is a single run of the experiment by a participant.
# Part          - A division of the experiment. Can be an abstract or concrete concept. 
#                 For example, a part can be a set of videos to be evaluated, or a set of questions to be answered.
#                 It is useful to divide the experiment into parts to make it easier to manage each session.
#                 The first part may contain the MUSHRA test page, the second part may contain the AB test page, and so on.
#                 But it is NOT required that every test page in a part be the same.
#                 Parts contain one or more (test) Pages. Parts can be randomized for each participant.
# Page          - A test page. It can be a MUSHRA test page, an AB test page, or any other *mode* of test page defined in /templates.
#                 A Page contains one unique ID (Name), its *mode* (MUSHRA, AB, etc.), and one or more stimuli to be evaluated.
#                 Pages can be randomized for each participant.
# Stimulus      - A content to be evaluated (currently, only videos). 
#                 A stimulus contains a unique ID (Name) and the path to the video file.
#                 Stimuli inside a Page can be randomized for each participant.
#
#
# The EXPERIMENT variable contains the experiment structure. It is a dictionary with the following keys:
# - Config: Contains the configuration for the experiment, also a dictionary:
#   - Random_part: If True, the order of the Parts will be randomized.
#   - Random_page: If True, the order of the Pages inside a Part will be randomized.
#   - VideoSource: The source of the videos. Can be 'local' or 'youtube'.
#                  (Only 'local' is fully implemented at the moment)
# - Parts: Every Part is defined by its name (key as string) and a list of Pages (values).
#          Create a new Part by adding a new key-value pair to the dictionary.
#
# A Page is defined as dictionary with the following keys:
# - Config: Contains the configuration for the Page, a dictionary:
#   - Mode: The mode of the test page. Can be 'MUSHRA', 'AB', 'Single', 'Single_v2', etc.
#           (See /templates for the available modes)
#   - Random: If True, the order of the stimuli will be randomized.
#   - Name: The name (ID) of the Page. This name will be used to save the results.
# - Stimulus: Every stimulus is defined by its name (key as string) and the path to the file (value).
#             Create a new stimulus by adding a new key-value pair to the dictionary.
#             Note: Some modes require a specific number of stimuli. Check the template for each mode.


HL_1 = {
    'Config': {
        'Mode': 'MUSHRA',
        'Random' : True,
        'Name': 'id01_p01_e03_f11_01000_15000',
    },
    'gt'   : 'data/HL/gt/id01_p01_e03_f11_01000_15000.mp4',
    'ptbr' : 'data/HL/ptbr/id01_p01_e03_f11_01000_15000.mp4',
    'zeggs': 'data/HL/zeggs/id01_p01_e03_f11_01000_15000.mp4',
}

HL_2 = {
    'Config': {
        'Mode': 'MUSHRA',
        'Random' : True,
        'Name': 'id01_p01_e03_f11_15000_25000',
    },
    'gt'   : 'data/HL/gt/id01_p01_e03_f11_15000_25000.mp4',
    'ptbr' : 'data/HL/ptbr/id01_p01_e03_f11_15000_25000.mp4',
    'zeggs': 'data/HL/zeggs/id01_p01_e03_f11_15000_25000.mp4',
}

HL_3 = {
    'Config': {
        'Mode': 'MUSHRA',
        'Random' : True,
        'Name': 'id01_p01_e03_f21_500_11000',
    },
    'gt'   : 'data/HL/gt/id01_p01_e03_f21_500_11000.mp4',
    'ptbr' : 'data/HL/ptbr/id01_p01_e03_f21_500_11000.mp4',
    'zeggs': 'data/HL/zeggs/id01_p01_e03_f21_500_11000.mp4',
}

HL_4 = {
    'Config': {
        'Mode': 'MUSHRA',
        'Random' : True,
        'Name': 'id01_p01_e03_f26_01000_13000',
    },
    'gt'   : 'data/HL/gt/id01_p01_e03_f26_01000_13000.mp4',
    'ptbr' : 'data/HL/ptbr/id01_p01_e03_f26_01000_13000.mp4',
    'zeggs': 'data/HL/zeggs/id01_p01_e03_f26_01000_13000.mp4',
}

HL_5 = {
    'Config': {
        'Mode': 'MUSHRA',
        'Random' : True,
        'Name': 'id02_p01_e03_f06_01500_11500',
    },
    'gt'   : 'data/HL/gt/id02_p01_e03_f06_01500_11500.mp4',
    'ptbr' : 'data/HL/ptbr/id02_p01_e03_f06_01500_11500.mp4',
    'zeggs': 'data/HL/zeggs/id02_p01_e03_f06_01500_11500.mp4',
}

HL_6 = {
    'Config': {
        'Mode': 'MUSHRA',
        'Random' : True,
        'Name': 'id02_p01_e03_f16_01000_13000',
    },
    'gt'   : 'data/HL/gt/id02_p01_e03_f16_01000_13000.mp4',
    'ptbr' : 'data/HL/ptbr/id02_p01_e03_f16_01000_13000.mp4',
    'zeggs': 'data/HL/zeggs/id02_p01_e03_f16_01000_13000.mp4',
}

HL_7 = {
    'Config': {
        'Mode': 'MUSHRA',
        'Random' : True,
        'Name': 'id02_p01_e03_f21_02500_18475',
    },
    'gt'   : 'data/HL/gt/id02_p01_e03_f21_02500_18475.mp4',
    'ptbr' : 'data/HL/ptbr/id02_p01_e03_f21_02500_18475.mp4',
    'zeggs': 'data/HL/zeggs/id02_p01_e03_f21_02500_18475.mp4',
}

HL_8 = {
    'Config': {
        'Mode': 'MUSHRA',
        'Random' : True,
        'Name': 'id02_p01_e03_f31_01000_16000',
    },
    'gt'   : 'data/HL/gt/id02_p01_e03_f31_01000_16000.mp4',
    'ptbr' : 'data/HL/ptbr/id02_p01_e03_f31_01000_16000.mp4',
    'zeggs': 'data/HL/zeggs/id02_p01_e03_f31_01000_16000.mp4',
}

APP_1 = {
    'Config': {
        'Mode': 'AB',
        'Random' : True,
        'Name': 'ptbr_id01_p01_e03_f21_11000_23000',
    },
    'Matched': 'data/APP/ptbr/Matched_id01_p01_e03_f21_11000_23000.mp4',
    'Mismatched': 'data/APP/ptbr/Mismatched_id01_p01_e03_f21_11000_23000.mp4',
}

APP_2 = {
    'Config': {
        'Mode': 'AB',
        'Random' : True,
        'Name': 'ptbr_id01_p01_e03_f31_16500_29500',
    },
    'Matched': 'data/APP/ptbr/Matched_id01_p01_e03_f31_16500_29500.mp4',
    'Mismatched': 'data/APP/ptbr/Mismatched_id01_p01_e03_f31_16500_29500.mp4',
}

APP_3 = {
    'Config': {
        'Mode': 'AB',
        'Random' : True,
        'Name': 'ptbr_id01_p01_e03_f41_500_12000',
    },
    'Matched': 'data/APP/ptbr/Matched_id01_p01_e03_f41_500_12000.mp4',
    'Mismatched': 'data/APP/ptbr/Mismatched_id01_p01_e03_f41_500_12000.mp4',
}

APP_4 = {
    'Config': {
        'Mode': 'AB',
        'Random' : True,
        'Name': 'ptbr_id02_p01_e03_f16_500_11000',
    },
    'Matched': 'data/APP/ptbr/Matched_id02_p01_e03_f16_500_11000.mp4',
    'Mismatched': 'data/APP/ptbr/Mismatched_id02_p01_e03_f16_500_11000.mp4',
}

APP_5 = {
    'Config': {
        'Mode': 'AB',
        'Random' : True,
        'Name': 'ptbr_id02_p01_e03_f26_01500_17500',
    },
    'Matched': 'data/APP/ptbr/Matched_id02_p01_e03_f26_01500_17500.mp4',
    'Mismatched': 'data/APP/ptbr/Mismatched_id02_p01_e03_f26_01500_17500.mp4',
}

APP_6 = {
    'Config': {
        'Mode': 'AB',
        'Random' : True,
        'Name': 'ptbr_id02_p01_e03_f36_01500_19200',
    },
    'Matched': 'data/APP/ptbr/Matched_id02_p01_e03_f36_01500_19200.mp4',
    'Mismatched': 'data/APP/ptbr/Mismatched_id02_p01_e03_f36_01500_19200.mp4',
}

APP_7 = {
    'Config': {
        'Mode': 'AB',
        'Random' : True,
        'Name': 'zeggs_id01_p01_e03_f21_11000_23000',
    },
    'Matched': 'data/APP/zeggs/Matched_id01_p01_e03_f21_11000_23000.mp4',
    'Mismatched': 'data/APP/zeggs/Mismatched_id01_p01_e03_f21_11000_23000.mp4',
}

APP_8 = {
    'Config': {
        'Mode': 'AB',
        'Random' : True,
        'Name': 'zeggs_id01_p01_e03_f31_16500_29500',
    },
    'Matched': 'data/APP/zeggs/Matched_id01_p01_e03_f31_16500_29500.mp4',
    'Mismatched': 'data/APP/zeggs/Mismatched_id01_p01_e03_f31_16500_29500.mp4',
}

APP_9 = {
    'Config': {
        'Mode': 'AB',
        'Random' : True,
        'Name': 'zeggs_id01_p01_e03_f41_500_12000',
    },
    'Matched': 'data/APP/zeggs/Matched_id01_p01_e03_f41_500_12000.mp4',
    'Mismatched': 'data/APP/zeggs/Mismatched_id01_p01_e03_f41_500_12000.mp4',
}

APP_10 = {
    'Config': {
        'Mode': 'AB',
        'Random' : True,
        'Name': 'zeggs_id02_p01_e03_f16_500_11000',
    },
    'Matched': 'data/APP/zeggs/Matched_id02_p01_e03_f16_500_11000.mp4',
    'Mismatched': 'data/APP/zeggs/Mismatched_id02_p01_e03_f16_500_11000.mp4',
}

APP_11 = {
    'Config': {
        'Mode': 'AB',
        'Random' : True,
        'Name': 'zeggs_id02_p01_e03_f26_01500_17500',
    },
    'Matched': 'data/APP/zeggs/Matched_id02_p01_e03_f26_01500_17500.mp4',
    'Mismatched': 'data/APP/zeggs/Mismatched_id02_p01_e03_f26_01500_17500.mp4',
}

APP_12 = {
    'Config': {
        'Mode': 'AB',
        'Random' : True,
        'Name': 'zeggs_id02_p01_e03_f36_01500_19200',
    },
    'Matched': 'data/APP/zeggs/Matched_id02_p01_e03_f36_01500_19200.mp4',
    'Mismatched': 'data/APP/zeggs/Mismatched_id02_p01_e03_f36_01500_19200.mp4',
}

APP_13 = {
    'Config': {
        'Mode': 'AB',
        'Random' : True,
        'Name': 'gt_id01_p01_e03_f21_11000_23000',
    },
    'Matched': 'data/APP/gt/Matched_id01_p01_e03_f21_11000_23000.mp4',
    'Mismatched': 'data/APP/gt/Mismatched_id01_p01_e03_f21_11000_23000.mp4',
}

APP_14 = {
    'Config': {
        'Mode': 'AB',
        'Random' : True,
        'Name': 'gt_id01_p01_e03_f31_16500_29500',
    },
    'Matched': 'data/APP/gt/Matched_id01_p01_e03_f31_16500_29500.mp4',
    'Mismatched': 'data/APP/gt/Mismatched_id01_p01_e03_f31_16500_29500.mp4',
}

APP_15 = {
    'Config': {
        'Mode': 'AB',
        'Random' : True,
        'Name': 'gt_id01_p01_e03_f41_500_12000',
    },
    'Matched': 'data/APP/gt/Matched_id01_p01_e03_f41_500_12000.mp4',
    'Mismatched': 'data/APP/gt/Mismatched_id01_p01_e03_f41_500_12000.mp4',
}

APP_16 = {
    'Config': {
        'Mode': 'AB',
        'Random' : True,
        'Name': 'gt_id02_p01_e03_f16_500_11000',
    },
    'Matched': 'data/APP/gt/Matched_id02_p01_e03_f16_500_11000.mp4',
    'Mismatched': 'data/APP/gt/Mismatched_id02_p01_e03_f16_500_11000.mp4',
}

APP_17 = {
    'Config': {
        'Mode': 'AB',
        'Random' : True,
        'Name': 'gt_id02_p01_e03_f26_01500_17500',
    },
    'Matched': 'data/APP/gt/Matched_id02_p01_e03_f26_01500_17500.mp4',
    'Mismatched': 'data/APP/gt/Mismatched_id02_p01_e03_f26_01500_17500.mp4',
}

APP_18 = {
    'Config': {
        'Mode': 'AB',
        'Random' : True,
        'Name': 'gt_id02_p01_e03_f36_01500_19200',
    },
    'Matched': 'data/APP/gt/Matched_id02_p01_e03_f36_01500_19200.mp4',
    'Mismatched': 'data/APP/gt/Mismatched_id02_p01_e03_f36_01500_19200.mp4',
}


PER_1 = {
    'Config': {
        'Mode': 'Single_v2',
        'Random' : True,
        'Name': 'ptbr_PER1_id01_e01',
    },
    'id01_e01': 'data/PER/ptbr/PER1_id01_p01_e01_f21_00500_14500.mp4',
}

PER_2 = {
    'Config': {
        'Mode': 'Single_v2',
        'Random' : True,
        'Name': 'ptbr_PER2_id01_e02',
    },
    'id01_e02': 'data/PER/ptbr/PER2_id01_p01_e02_f11_01000_16000.mp4',
}

PER_3 = {
    'Config': {
        'Mode': 'Single_v2',
        'Random' : True,
        'Name': 'ptbr_PER3_id01_e03',
    },
    'id01_e03': 'data/PER/ptbr/PER3_d01_p01_e03_f16_00500_14000.mp4',
}

PER_4 = {
    'Config': {
        'Mode': 'Single_v2',
        'Random' : True,
        'Name': 'ptbr_PER1_id02_e01',
    },
    'id02_e01': 'data/PER/ptbr/PER1_id02_p01_e01_f36_08000_25000.mp4',
}

PER_5 = {
    'Config': {
        'Mode': 'Single_v2',
        'Random' : True,
        'Name': 'ptbr_PER1_id02_e02',
    },
    'id02_e02': 'data/PER/ptbr/PER2_id02_p01_e02_f41_01000_16000.mp4',
}

PER_6 = {
    'Config': {
        'Mode': 'Single_v2',
        'Random' : True,
        'Name': 'ptbr_PER1_id02_e03',
    },
    'id02_e03': 'data/PER/ptbr/PER3_id02_p01_e03_f31_01500_13500.mp4',
}

PER_7 = {
    'Config': {
        'Mode': 'Single_v2',
        'Random' : True,
        'Name': 'zeggs_PER1_id01_e01',
    },
    'id01_e01': 'data/PER/zeggs/PER1_id01_p01_e01_f41_01000_13000.mp4',
}

PER_8 = {
    'Config': {
        'Mode': 'Single_v2',
        'Random' : True,
        'Name': 'zeggs_PER2_id01_e02',
    },
    'id01_e02': 'data/PER/zeggs/PER2_id01_p01_e02_f31_02000_14000.mp4',
}

PER_9 = {
    'Config': {
        'Mode': 'Single_v2',
        'Random' : True,
        'Name': 'zeggs_PER3_id01_e03',
    },
    'id01_e03': 'data/PER/zeggs/PER3_id01_p01_e03_f21_01000_13000.mp4',
}

PER_10 = {
    'Config': {
        'Mode': 'Single_v2',
        'Random' : True,
        'Name': 'zeggs_PER1_id02_e01',
    },
    'id02_e01': 'data/PER/zeggs/PER1_id02_p01_e01_f26_01000_11000.mp4',
}

PER_11 = {
    'Config': {
        'Mode': 'Single_v2',
        'Random' : True,
        'Name': 'zeggs_PER1_id02_e02',
    },
    'id02_e02': 'data/PER/zeggs/PER2_id02_p01_e02_f06_02000_13000.mp4',
}

PER_12 = {
    'Config': {
        'Mode': 'Single_v2',
        'Random' : True,
        'Name': 'zeggs_PER1_id02_e03',
    },
    'id02_e03': 'data/PER/zeggs/PER3_id02_p01_e03_f01_01000_13000.mp4',
}

PER_13 = {
    'Config': {
        'Mode': 'Single_v2',
        'Random' : True,
        'Name': 'gt_PER1_id01_e01',
    },
    'id01_e01': 'data/PER/gt/PER1_id01_p01_e01_f16_0500_10500.mp4',
}

PER_14 = {
    'Config': {
        'Mode': 'Single_v2',
        'Random' : True,
        'Name': 'gt_PER2_id01_e02',
    },
    'id01_e02': 'data/PER/gt/PER2_id01_p01_e02_f26_01000_13000.mp4',
}

PER_15 = {
    'Config': {
        'Mode': 'Single_v2',
        'Random' : True,
        'Name': 'gt_PER3_id01_e03',
    },
    'id01_e03': 'data/PER/gt/PER3_id01_p01_e03_f01_01000_13000.mp4',
}

PER_16 = {
    'Config': {
        'Mode': 'Single_v2',
        'Random' : True,
        'Name': 'gt_PER1_id02_e01',
    },
    'id02_e01': 'data/PER/gt/PER1_id02_p01_e01_f06_01000_11000.mp4',
}

PER_17 = {
    'Config': {
        'Mode': 'Single_v2',
        'Random' : True,
        'Name': 'gt_PER1_id02_e02',
    },
    'id02_e02': 'data/PER/gt/PER2_id02_p01_e02_f36_02000_14000.mp4',
}

PER_18 = {
    'Config': {
        'Mode': 'Single_v2',
        'Random' : True,
        'Name': 'gt_PER1_id02_e03',
    },
    'id02_e03': 'data/PER/gt/PER3_id02_p01_e03_f21_01500_11500.mp4',
}

EST_1 = {
    'Config': {
        'Mode': 'Single',
        'Random' : True,
        'Name': 'ptbr_id01_e01',
    },
    'ptbr_id01_p02_e01_f00': 'data/EST/ptbr/id01_p02_e01_f00.mp4',
}

EST_2 = {
    'Config': {
        'Mode': 'Single',
        'Random' : True,
        'Name': 'ptbr_id01_e02',
    },
    'ptbr_id01_p02_e02_f27': 'data/EST/ptbr/id01_p02_e02_f27.mp4',
}

EST_3 = {
    'Config': {
        'Mode': 'Single',
        'Random' : True,
        'Name': 'ptbr_id01_e03',
    },
    'ptbr_id01_p02_e03_f12': 'data/EST/ptbr/id01_p02_e03_f12.mp4',
}

EST_4 = {
    'Config': {
        'Mode': 'Single',
        'Random' : True,
        'Name': 'ptbr_id02_e01',
    },
    'ptbr_id02_p02_e01_f15': 'data/EST/ptbr/id02_p02_e01_f15.mp4',
}

EST_5 = {
    'Config': {
        'Mode': 'Single',
        'Random' : True,
        'Name': 'ptbr_id02_e02',
    },
    'ptbr_id02_p02_e02_f48': 'data/EST/ptbr/id02_p02_e02_f48.mp4',
}

EST_6 = {
    'Config': {
        'Mode': 'Single',
        'Random' : True,
        'Name': 'ptbr_id02_e03',
    },
    'ptbr_id02_p02_e03_f09_01000_18000': 'data/EST/ptbr/id02_p02_e03_f09_01000_18000.mp4',
}

EST_7 = {
    'Config': {
        'Mode': 'Single',
        'Random' : True,
        'Name': 'zeggs_id01_e01',
    },
    'zeggs_id01_p02_e01_f00': 'data/EST/zeggs/id01_p02_e01_f00.mp4',
}

EST_8 = {
    'Config': {
        'Mode': 'Single',
        'Random' : True,
        'Name': 'zeggs_id01_e02',
    },
    'zeggs_id01_p02_e02_f27': 'data/EST/zeggs/id01_p02_e02_f27.mp4',
}

EST_9 = {
    'Config': {
        'Mode': 'Single',
        'Random' : True,
        'Name': 'zeggs_id01_e03',
    },
    'zeggs_id01_p02_e03_f12': 'data/EST/zeggs/id01_p02_e03_f12.mp4',
}

EST_10 = {
    'Config': {
        'Mode': 'Single',
        'Random' : True,
        'Name': 'zeggs_id02_e01',
    },
    'zeggs_id02_p02_e01_f15': 'data/EST/zeggs/id02_p02_e01_f15.mp4',
}

EST_11 = {
    'Config': {
        'Mode': 'Single',
        'Random' : True,
        'Name': 'zeggs_id02_e02',
    },
    'zeggs_id02_p02_e02_f48': 'data/EST/zeggs/id02_p02_e02_f48.mp4',
}

EST_12 = {
    'Config': {
        'Mode': 'Single',
        'Random' : True,
        'Name': 'zeggs_id02_e03',
    },
    'zeggs_id02_p02_e03_f09_01000_18000': 'data/EST/zeggs/id02_p02_e03_f09_01000_18000.mp4',
}

EST_13 = {
    'Config': {
        'Mode': 'Single',
        'Random' : True,
        'Name': 'gt_id01_e01',
    },
    'gt_id01_p02_e01_f00': 'data/EST/gt/id01_p02_e01_f00.mp4',
}

EST_14 = {
    'Config': {
        'Mode': 'Single',
        'Random' : True,
        'Name': 'gt_id01_e02',
    },
    'gt_id01_p02_e02_f27': 'data/EST/gt/id01_p02_e02_f27.mp4',
}

EST_15 = {
    'Config': {
        'Mode': 'Single',
        'Random' : True,
        'Name': 'gt_id01_e03',
    },
    'gt_id01_p02_e03_f12': 'data/EST/gt/id01_p02_e03_f12.mp4',
}

EST_16 = {
    'Config': {
        'Mode': 'Single',
        'Random' : True,
        'Name': 'gt_id02_e01',
    },
    'gt_id02_p02_e01_f15': 'data/EST/gt/id02_p02_e01_f15.mp4',
}

EST_17 = {
    'Config': {
        'Mode': 'Single',
        'Random' : True,
        'Name': 'gt_id02_e02',
    },
    'gt_id02_p02_e02_f48': 'data/EST/gt/id02_p02_e02_f48.mp4',
}

EST_18 = {
    'Config': {
        'Mode': 'Single',
        'Random' : True,
        'Name': 'gt_id02_e03',
    },
    'gt_id02_p02_e03_f09_01000_18000': 'data/EST/gt/id02_p02_e03_f09_01000_18000.mp4',
}

EXPERIMENT = {
    'Config'      : {
        'Random_part' : False,
        'Random_page' : True,
        'VideoSource' : 'local', # youtube or local
    },
    'Part1'          : [HL_1, HL_2, HL_3, HL_4, HL_5, HL_6, HL_7, HL_8],
    'Part2'          : [APP_1, APP_2, APP_3, APP_4, APP_5, APP_6, APP_7, APP_8, APP_9, APP_10, APP_11, APP_12, APP_13, APP_14, APP_15, APP_16, APP_17, APP_18],
    'Part3'          : [PER_1, PER_2, PER_3, PER_4, PER_5, PER_6, PER_7, PER_8, PER_9, PER_10, PER_11, PER_12, PER_13, PER_14, PER_15, PER_16, PER_17, PER_18],
    'Part4'          : [EST_1, EST_2, EST_3, EST_4, EST_5, EST_6, EST_7, EST_8, EST_9, EST_10, EST_11, EST_12, EST_13, EST_14, EST_15, EST_16, EST_17, EST_18],
    # For debugging:
    #'Part1'          : [HL_1],
    #Part2'           : [APP_1],
    #'Part3'          : [PER_1],
    #'Part4'          : [EST_1],
}


# Use this if using embedded youtube videos
# VIDEO_PARAMS = '?autoplay=0&controls=0&mute=0&loop=0&start=0&end=0&rel=0&modestbranding=1&showinfo=0&enablejsapi=1&color=red'

# Use this if using youtube API
VIDEO_PARAMS = { 'autoplay': 0,
                   'color': 'red',
                   'controls': 0,
                   'disablekb': 1,
                   'enablejsapi': 1,
                   'mute': 0,
                   'loop': 0,
                   'modestbranding': 1,
                   'playsinline': 1,
                   'start': 0,
                   'rel': 0,
                   'showinfo': 0,
                 }
