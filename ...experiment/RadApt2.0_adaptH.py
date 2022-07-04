# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 15:09:05 2022

@author: Pauline + Alexia

Experiment: Radial adaptation

This experiment measures the radial bias at 15° of eccentricity
        left & right horizontal meridian
        upper & lower vertical meridian

        using a 4AFC task (where is the stimulus, left/right/up/down)
        and a diy staircase that allows to spend more trials on lower contrast levels

In 3 conditions of adaptation (with full field 1/f noise)
        Isotropic
        Horizontal 
        Vertical

"""

#%%#   Import packages

from psychopy import core, visual, gui, data, event, monitors, sound
import numpy as np
import pandas as pd
import os
import random
import pickle
practice = 'no' #whether to do the practice pgase (yes or no)


#%%#  Path stuff

# Print the current working directory
print("Current working directory: {0}".format(os.getcwd()))


# Change the current working directory HERE
# cwd = os.chdir(r'C:\Users\alexi\OneDrive - UCL\Rprojects\2022_RadApt_filterednoise\...experiment')
# cwd = os.chdir(r'C:\Users\humanvisionlab\Documents\dossierpartageubuntu\Pauline\RadApt_filterednoise\...experiment')
cmd = os.chdir(r'C:\Users\arouxsibilon\OneDrive - UCL\Rprojects\2022_RadApt_filterednoise\...experiment')


print("Current working directory: {0}".format(os.getcwd()))
cwd = format(os.getcwd())

stimdir = cwd + '\stim\\' #directory where the stimuli are
datadir = cwd + '\data\\' #directory to save data in



#%%#
'''
Open dlg box, Store info about the experiment session
Check whether it is the 1st session. If not, load pickled objects
'''

# Get subject's info through a dialog box
exp_name = 'RadApt1.0'
exp_info = {
    'subj_ID': '',
    'session': ''
    }

dlg = gui.DlgFromDict(dictionary = exp_info, title = exp_name) # Open a dialog box
if dlg.OK == False: # If 'Cancel' is pressed, quit
    core.quit()
        
# Get date and time
exp_info['date'] = data.getDateStr()
exp_info['exp_name'] = exp_name
subj_ID = exp_info['subj_ID']
date = exp_info['date']



#%%#
'''
Define / initialize some variables that will be usefull later
'''

# Number of trials that we want for each condition (e.g., condition [adapter = ISO, VF = left, orientation = horizontal])
nTrialsPerStaircase = 2

# max time (in s) to wait for a response
timelimit = 10 

# fixation colors
neutralColor = (-1, -1, -1)
waitColor = (-0.2, -0.2, -0.2) #for when waiting for a response
notOKcolor = (-1, 0, -1) 
OKcolor = (0, -1, -1) #both these colors look weird with the texture that
                        #makes the fixation, but it is ok (notOKcolor is pinkish, OKcolor is blueish)

### Parameters of the adapter stimulus
NBnoiseSamples = list(range(10))  # Number of noise samples in the adapter stimulus
adaptSize = 2199
isoOri = 0
horizOri = 90
vertOri = 0
# size of the adapter + gaussian background
bgSize = 2199 


#%%#  Define parameters of the Patch stim
patchSizeDVA = 6
patchSize = 200 # Size in pixels (15° ecc condition)

# Where to present the stim (eccentricity)
left_xpos15 = -502
right_xpos15 = 502
up_ypos15 = 502
down_ypos15 = -502

patchDuration = 0.150 # Presentation duration

# Contrasts levels, just for the demo/training phase 
#NB 0 = uniform (no contrast), 1 = maximum contrast
contrastLevels = np.around(list(np.arange(0.5,1,0.1)),1)
contrastLevels = contrastLevels.tolist()            
# High contrasts levels, for the test phase 
highContrastLevels = np.around(list(np.arange(0.2,0.6,0.02)),2)
highContrastLevels = highContrastLevels.tolist()    
np.random.shuffle(highContrastLevels)


### Parameters of the staircase
ndown = 2 # Nb of correct responses before decreasing the contrast
nup = 1 # Nb of incorrect responses before increasing the contrast
down_step = 0.02
up_step = 0.03
maxContrast = 0.2


#%%#
'''
Make trial list for this subject.
(on the first session. On the next sessions, the pickled trial list will be loaded)
'''
triallist = [
    {'adapter':'adapterH','eccentricity':'15dva','VF':'left','ori':'oriH','patch':0},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'left','ori':'oriV','patch':0},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'right','ori':'oriH','patch':0},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'right','ori':'oriV','patch':0},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'up','ori':'oriH','patch':0},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'up','ori':'oriV','patch':0},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'down','ori':'oriH','patch':0},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'down','ori':'oriV','patch':0},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'left','ori':'oriH','patch':1},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'left','ori':'oriV','patch':1},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'right','ori':'oriH','patch':1},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'right','ori':'oriV','patch':1},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'up','ori':'oriH','patch':1},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'up','ori':'oriV','patch':1},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'down','ori':'oriH','patch':1},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'down','ori':'oriV','patch':1},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'left','ori':'oriH','patch':2},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'left','ori':'oriV','patch':2},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'right','ori':'oriH','patch':2},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'right','ori':'oriV','patch':2},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'up','ori':'oriH','patch':2},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'up','ori':'oriV','patch':2},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'down','ori':'oriH','patch':2},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'down','ori':'oriV','patch':2},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'left','ori':'oriH','patch':3},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'left','ori':'oriV','patch':3},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'right','ori':'oriH','patch':3},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'right','ori':'oriV','patch':3},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'up','ori':'oriH','patch':3},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'up','ori':'oriV','patch':3},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'down','ori':'oriH','patch':3},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'down','ori':'oriV','patch':3},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'left','ori':'oriH','patch':4},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'left','ori':'oriV','patch':4},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'right','ori':'oriH','patch':4},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'right','ori':'oriV','patch':4},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'up','ori':'oriH','patch':4},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'up','ori':'oriV','patch':4},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'down','ori':'oriH','patch':4},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'down','ori':'oriV','patch':4},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'left','ori':'oriH','patch':5},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'left','ori':'oriV','patch':5},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'right','ori':'oriH','patch':5},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'right','ori':'oriV','patch':5},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'up','ori':'oriH','patch':5},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'up','ori':'oriV','patch':5},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'down','ori':'oriH','patch':5},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'down','ori':'oriV','patch':5},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'left','ori':'oriH','patch':6},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'left','ori':'oriV','patch':6},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'right','ori':'oriH','patch':6},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'right','ori':'oriV','patch':6},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'up','ori':'oriH','patch':6},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'up','ori':'oriV','patch':6},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'down','ori':'oriH','patch':6},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'down','ori':'oriV','patch':6},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'left','ori':'oriH','patch':7},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'left','ori':'oriV','patch':7},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'right','ori':'oriH','patch':7},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'right','ori':'oriV','patch':7},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'up','ori':'oriH','patch':7},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'up','ori':'oriV','patch':7},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'down','ori':'oriH','patch':7},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'down','ori':'oriV','patch':7},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'left','ori':'oriH','patch':8},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'left','ori':'oriV','patch':8},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'right','ori':'oriH','patch':8},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'right','ori':'oriV','patch':8},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'up','ori':'oriH','patch':8},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'up','ori':'oriV','patch':8},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'down','ori':'oriH','patch':8},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'down','ori':'oriV','patch':8},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'left','ori':'oriH','patch':9},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'left','ori':'oriV','patch':9},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'right','ori':'oriH','patch':9},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'right','ori':'oriV','patch':9},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'up','ori':'oriH','patch':9},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'up','ori':'oriV','patch':9},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'down','ori':'oriH','patch':9},
    {'adapter':'adapterH','eccentricity':'15dva','VF':'down','ori':'oriV','patch':9}
    ]                     


for i in range(int(nTrialsPerStaircase/10)-1):
    h_template = [
        {'adapter':'adapterH','eccentricity':'15dva','VF':'left','ori':'oriH','patch':0},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'left','ori':'oriV','patch':0},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'right','ori':'oriH','patch':0},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'right','ori':'oriV','patch':0},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'up','ori':'oriH','patch':0},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'up','ori':'oriV','patch':0},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'down','ori':'oriH','patch':0},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'down','ori':'oriV','patch':0},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'left','ori':'oriH','patch':1},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'left','ori':'oriV','patch':1},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'right','ori':'oriH','patch':1},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'right','ori':'oriV','patch':1},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'up','ori':'oriH','patch':1},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'up','ori':'oriV','patch':1},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'down','ori':'oriH','patch':1},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'down','ori':'oriV','patch':1},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'left','ori':'oriH','patch':2},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'left','ori':'oriV','patch':2},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'right','ori':'oriH','patch':2},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'right','ori':'oriV','patch':2},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'up','ori':'oriH','patch':2},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'up','ori':'oriV','patch':2},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'down','ori':'oriH','patch':2},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'down','ori':'oriV','patch':2},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'left','ori':'oriH','patch':3},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'left','ori':'oriV','patch':3},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'right','ori':'oriH','patch':3},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'right','ori':'oriV','patch':3},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'up','ori':'oriH','patch':3},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'up','ori':'oriV','patch':3},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'down','ori':'oriH','patch':3},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'down','ori':'oriV','patch':3},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'left','ori':'oriH','patch':4},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'left','ori':'oriV','patch':4},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'right','ori':'oriH','patch':4},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'right','ori':'oriV','patch':4},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'up','ori':'oriH','patch':4},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'up','ori':'oriV','patch':4},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'down','ori':'oriH','patch':4},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'down','ori':'oriV','patch':4},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'left','ori':'oriH','patch':5},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'left','ori':'oriV','patch':5},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'right','ori':'oriH','patch':5},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'right','ori':'oriV','patch':5},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'up','ori':'oriH','patch':5},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'up','ori':'oriV','patch':5},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'down','ori':'oriH','patch':5},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'down','ori':'oriV','patch':5},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'left','ori':'oriH','patch':6},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'left','ori':'oriV','patch':6},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'right','ori':'oriH','patch':6},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'right','ori':'oriV','patch':6},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'up','ori':'oriH','patch':6},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'up','ori':'oriV','patch':6},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'down','ori':'oriH','patch':6},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'down','ori':'oriV','patch':6},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'left','ori':'oriH','patch':7},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'left','ori':'oriV','patch':7},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'right','ori':'oriH','patch':7},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'right','ori':'oriV','patch':7},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'up','ori':'oriH','patch':7},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'up','ori':'oriV','patch':7},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'down','ori':'oriH','patch':7},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'down','ori':'oriV','patch':7},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'left','ori':'oriH','patch':8},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'left','ori':'oriV','patch':8},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'right','ori':'oriH','patch':8},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'right','ori':'oriV','patch':8},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'up','ori':'oriH','patch':8},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'up','ori':'oriV','patch':8},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'down','ori':'oriH','patch':8},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'down','ori':'oriV','patch':8},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'left','ori':'oriH','patch':9},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'left','ori':'oriV','patch':9},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'right','ori':'oriH','patch':9},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'right','ori':'oriV','patch':9},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'up','ori':'oriH','patch':9},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'up','ori':'oriV','patch':9},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'down','ori':'oriH','patch':9},
        {'adapter':'adapterH','eccentricity':'15dva','VF':'down','ori':'oriV','patch':9}
    ]
    triallist.extend(h_template)
random.shuffle(triallist)


    
# nb trials...
nTrialsTotal = len(triallist)
totalTime = nTrialsTotal*7/60/60 #approximative total time in hours



#%%#
'''
Prepare window object and stimuli
'''
# Window object
OLED = monitors.Monitor('testmonitor') #on changera ça après avoir mesuré la gamma
OLED.setSizePix((3840, 2160)) 
win = visual.Window(monitor = OLED,
                    color = (-1, -1, -1),
                    units = 'pix',
                    fullscr = True,
                    allowGUI = False)
win.setMouseVisible(False)

# Fixation dot
#########################
fix = np.ones((20, 20))*(-1)
fixation = visual.GratingStim(win, tex=fix, mask='gauss', units='pix', size=20      )    

# Patch Stimuli
###################
# Create base object to host the different versions of the patch stimulus
patch1f = os.path.join(stimdir + 'patch1.bmp') 
patch2f = os.path.join(stimdir + 'patch2.bmp') 
patch3f = os.path.join(stimdir + 'patch3.bmp') 
patch4f = os.path.join(stimdir + 'patch4.bmp') 
patch5f = os.path.join(stimdir + 'patch5.bmp') 
patch6f = os.path.join(stimdir + 'patch6.bmp') 
patch7f = os.path.join(stimdir + 'patch7.bmp') 
patch8f = os.path.join(stimdir + 'patch8.bmp') 
patch9f = os.path.join(stimdir + 'patch9.bmp') 
patch10f = os.path.join(stimdir + 'patch10.bmp') 

patchSamples = [patch1f,patch2f,patch3f,patch4f,patch5f,patch6f,patch7f,patch8f,patch9f,patch10f]

patch = visual.ImageStim(win,
                         units = 'pix', pos = (0,0), 
                         size = (patchSize,patchSize))

# Little Bip sound 
######################
bleepf = os.path.join(stimdir + 'blip.wav')
bleep = sound.Sound(value=bleepf) 

# Gaussian Gray background
##############################
gaussianGrayf = os.path.join(stimdir + 'gaussianGray.bmp') 
gaussianGray = visual.ImageStim(win, image = gaussianGrayf,
                                units = 'pix', pos = (0,0), 
                                size = (bgSize,bgSize))

# Pause text
################
pause = visual.TextStim(win, color = (-1, -1, -0.5))
   
# Adapter stimuli 
#####################
# Create base object to host the sample images
adaptHost = visual.ImageStim(win, units = 'pix', pos = (0,0), 
                            size = (adaptSize,adaptSize))

# Define function that draws the different images for the HORIZONTAL adapter
def drawAdapter():
    for i in NBnoiseSamples:
        x = i+1
        fname = os.path.join(stimdir + 'sample' + str(x) + '.bmp')
        adaptHost.setImage(fname)
        adaptHost.ori = horizOri
        adaptHost.draw()
        fixation.draw()
        win.flip()
        core.wait(0.1)
    
        

#%%#
'''
Prepare staircases
'''
thisCond = [] 
condition_names = ['adapterH_left_oriH', 'adapterH_left_oriV',
                  'adapterH_right_oriH', 'adapterH_right_oriV',
                  'adapterH_up_oriH', 'adapterH_up_oriV',
                  'adapterH_down_oriH', 'adapterH_down_oriV'
                  ]

value = 0

contrast_dict    = {key:value for key in condition_names}
acc_count_dict   = {key:value for key in condition_names}
trial_count_dict = {key:value for key in condition_names}    


    
# ###  Define staircase function
def staircase(condition):
    # we need to work with the global variables (so that they can be used 
    # outside of the function)
    global thisCond
    global contrast_dict
    global acc_count_dict
    global trial_count_dict
  
    # 1st trial: set the initial contrast value as the value defined in maxContrast
    if trial_count_dict[thisCond] == 1: 
        contrast_dict[thisCond] = contrast_dict[thisCond] + maxContrast
    
    # From the 2nd trial:
    elif trial_count_dict[thisCond] > 1: 
        
            # if acc = 0 at last trial, increases contrast level
            if acc_count_dict[thisCond] == 0: 
                contrast_dict[thisCond] = abs(contrast_dict[thisCond] + up_step)
            # if acc = 1 at last trial, first time, keep the same contrast level
            elif (acc_count_dict[thisCond] > 0) & (acc_count_dict[thisCond] < ndown): 
                contrast_dict[thisCond] = abs(contrast_dict[thisCond]) 
            # if acc = 1 at last trial, second time, decrease contrast level
            else: # (acc_count_dict[thisCond] == ndown):
                contrast_dict[thisCond] = abs(contrast_dict[thisCond] - down_step)
                acc_count_dict[thisCond] = 0  
                
                
                




#%%#
'''
BEGIN EXPERIMENT
'''

    
# Draw the windows onto the screen
win.flip()


'''
Instructions
'''

'''
Practice {TO DO}
'''

'''
TEST LOOP
'''

# Initialize output arrays
trainingtest_array = []
trial_array = []
adaptation_array = []
eccentricity_array = []
xPos_array = []
yPos_array = []
meridian_array = []
contrast_array = []
patch_ori_array = []
VF_array = []
resp_array = []
accuracy_array = []
accCount_array = []
thisCond_array = []
trialCount_array = []
contrastRule_array = []


win.flip()

trial = 0

for thisTrial in range(len(triallist)): 
    
    
    ''' Prepare trial '''
    trial = trial + 1 # this is just trial number, to append to data file
    
    theTrial = triallist[thisTrial]
    theAdapter = theTrial['adapter']
    theEccentricity = theTrial['eccentricity']  
    theVF = theTrial['VF']
    theOri = theTrial['ori']
    thePatch = theTrial['patch']
    if (theVF == 'left') or (theVF == 'right'):
        theMeridian = "meridianH"
    else:
        theMeridian  = "meridianV"
    
    thisCond = theAdapter + '_' + theVF + '_' + theOri    
    trial_count_dict[thisCond] = trial_count_dict[thisCond] + 1

    # Set patch sample
    patch.setImage(patchSamples[thePatch])

        
    # Set patch position depending on the condition
    if (theVF == 'left'):
        yPos = 0 # horizontal meridian --> y = 0
        xPos = left_xpos15
    elif (theVF == 'right'):
        yPos = 0 # horizontal meridian --> y = 0
        xPos = right_xpos15
    elif (theVF == 'up'):
        xPos = 0 # vertical meridian --> x = 0
        yPos = up_ypos15
    elif (theVF == 'down'):
        xPos = 0 # vertical meridian --> x = 0
        yPos = down_ypos15
    patch.pos = (xPos,yPos)

    # Set patch orientation
    if theOri == 'oriH':
        ori = 90
    else:
        ori = 0    
    patch.ori = ori

        
    # Set patch contrast 
    # ... either pick within higher contrast range
    if (trial_count_dict[thisCond]%5 == 0):
        zecontrast = random.choice(highContrastLevels)
        patch.contrast = zecontrast
    # ... or use staircase rules      
    else:
        staircase(thisCond)
        patch.contrast = abs(contrast_dict[thisCond])
                
        
    ''' Draw stimuli on screen '''
    # Draw adapter       
    if (thisTrial%25 == 0):
        for x in range(9): # Adapter is on screen for 10 sec
            drawAdapter()
    else:
        for x in range(4): # Adapter is on screen for 10 sec
            drawAdapter()
            
    # Draw fixation
    gaussianGray.draw()
    fixation.color = neutralColor
    fixation.draw()
    win.flip()
    core.wait(0.5) # wait for 500ms
        
    # Draw stimulus
    gaussianGray.draw()
    patch.draw()
    fixation.draw()
    # bleep.play()
    win.flip()
    core.wait(patchDuration) 
    gaussianGray.draw()
    fixation.color = waitColor
    fixation.draw()
    win.flip()
    event.clearEvents()
    keys = event.waitKeys(maxWait=timelimit, keyList=['left', 'right', 'up', 'down', 'q'])
    
    
    ''' Take response, calculate accuracy and give feedback (fixation color) '''
     # If a key is pressed, take the response. If not, just remove the images from the screen    
    if keys:
        resp = keys[0]
                                    
        #At this point, there are still no keys pressed. So "if not keys" is definitely 
        #going to be processed.
        #After removing the images from the screen, still listening for a keypress. 
        #Record the reaction time if a key is pressed.
                                    
    if not keys:            
        keys = event.waitKeys(maxWait = timelimit, keyList=['left', 'right', 'up', 'down', 'q'])
    

                              
    # If the key is pressed analyze the keypress.
    if keys:
        if 'q' in keys:
            break
            win.close()
            core.quit()
        else:
            resp = keys[0]
    else: 
        resp = 'noResp'
        
    # Check accuracy
    if resp == theVF:
        acc = 1
        acc_count_dict[thisCond] = acc_count_dict[thisCond] + 1
    elif resp == 'noResp':
        acc = 0
        acc_count_dict[thisCond] = 0
    else:
        acc = 0
        acc_count_dict[thisCond] = 0
    
    # ISI ... (+ change fixation dot color depending on accuracy)
    if acc == 1:
        accColor = OKcolor
    else:
        accColor = notOKcolor
    
    gaussianGray.draw()
    fixation.color = accColor
    fixation.draw()
    win.flip()
    core.wait(0.5) # wait 
    gaussianGray.draw()
    fixation.color = neutralColor
    fixation.draw()
    win.flip()
    core.wait(1) # wait 
    
    
    ''' Save information about the trial '''
    trial_array.append(trial)
    trainingtest_array.append('test')
    adaptation_array.append(theAdapter)
    eccentricity_array.append(theEccentricity)
    meridian_array.append(theMeridian)
    VF_array.append(theVF)
    patch_ori_array.append(theOri)
    xPos_array.append(xPos)
    yPos_array.append(yPos)
    resp_array.append(resp)
    accuracy_array.append(acc)
    accCount_array.append(acc_count_dict[thisCond])
    thisCond_array.append(thisCond)
    trialCount_array.append(trial_count_dict[thisCond])
    if (trial_count_dict[thisCond]%5 == 0):
        contrast_array.append(zecontrast)
        contrastRule_array.append("highCont")  
    else:
        contrastRule_array.append("staircase")
        contrast_array.append(contrast_dict[thisCond])
        
        
    
    ''' Should we make a small break, or stop the experiment for today? ''' 
    # Small pause every 25 trials
    if (trial%25 == 0):
        progression = round(trial*100/nTrialsTotal, 2)
        progressionSession = round(trial*100/(nTrialsTotal), 2)
        pause_txt = 'Take a little break : ) \n Progression: \n ' + str(progressionSession) + '% of this session \n' + str(progression) + '% of the entire experiment' +'\n \n Press SPACE to resume'
        pause.setText(pause_txt)
        gaussianGray.draw()
        pause.draw()
        win.flip() 
        event.clearEvents()
        keys = event.waitKeys(keyList=['space', 'q'])
        if 'q' in keys:
            break
            win.close()
            core.quit()
        if 'space' in keys:
            gaussianGray.draw()
            win.flip()
            core.wait(2)
    # If an adaptation phase is finished, quit the experiment for now
    if trial == nTrialsTotal:
        end_txt = 'Bravo! You just finished this session. \n You will resume the experiment another time \n Press q to quit, the experimenter will come soon.'
        pause.setText(end_txt)
        gaussianGray.draw()
        pause.draw()
        win.flip() 
        event.clearEvents()
        keys = event.waitKeys(keyList=['q'])
        if 'q' in keys:
            break
            win.close()
            core.quit()
        win.flip() 



#%%#
'''
Save data and pickle some objects for the next session
'''

win.close()


    
    
### Save data as pickle + csv

if not os.path.isdir(datadir):
    os.makedirs(datadir)
data_fname = exp_info['subj_ID'] + '_' + exp_name +  '_session'+ exp_info['session'] + '_' + exp_info['date'] + '.csv'
data_fname = os.path.join(datadir, data_fname)

actualNtrials = len(contrastRule_array)

subject_array = []
exp_name_array = []
date_array = [] 
session_array = []
patchSize_array = []
patchSizeDVA_array = []
for n in range(actualNtrials):
    subject_array.append(exp_info['subj_ID'])
    exp_name_array.append(exp_name)
    date_array.append(exp_info['date'])
    session_array.append(exp_info['session'])
    patchSize_array.append(patchSize)
    patchSizeDVA_array.append(patchSizeDVA)
    
    

output_file = pd.DataFrame({'subj_ID': subject_array,
                            'exp_name': exp_name_array,
                            'date': date_array,
                            'session': session_array,
                            'patchSizeDVA': patchSizeDVA_array,
                            'patchSize': patchSize_array,
                            'trial': trial_array,
                            'condition': thisCond_array,
                            'adaptation': adaptation_array,
                            'eccentricity': eccentricity_array,
                            'meridian': meridian_array,
                            'VF': VF_array,
                            'ori': patch_ori_array,
                            'xPosition': xPos_array,
                            'yPosition': yPos_array,
                            'contrast': contrast_array,
                            'resp': resp_array,
                            'accuracy': accuracy_array,
                            'accCount': accCount_array,
                            'trialCount': trialCount_array,
                            'contrastRule': contrastRule_array
                            })

# save the csv file + pickle

# CSV file
output_file.to_csv(data_fname, index = False)

# Pickle
with open(data_fname + ".pkl", 'wb') as f:
    pickle.dump(output_file, f, pickle.HIGHEST_PROTOCOL)
   
print('FILES SAVED')

