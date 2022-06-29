# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 15:47:30 2022

@author: Pauline + Alexia

Experiment: Radial adaptation: filtered noise

This is the 1st part of the experiment.

This program simply measures the BASELINE RADIAL BIAS with FILTERED NOISE PATCHES

- 1 ecc = 15°

- 4AFC TASK !! 
"""

#%%#   Import packages

from psychopy import core, visual, gui, data, event, monitors, sound
import numpy as np
import pandas as pd
import os
import random

practice = 'no' #whether to do the practice (yes or no)


#%%#  Path stuff

# Print the current working directory
print("Current working directory: {0}".format(os.getcwd()))

# Change the current working directory HERE
cwd = os.chdir(r'C:\Users\alexi\OneDrive - UCL\Rprojects\2022_RadApt_filterednoise\...experiment')
# cwd = os.chdir(r'C:\Users\humanvisionlab\Documents\dossierpartageubuntu\Pauline\RadApt_filterednoise\...experiment')
#cmd = os.chdir(r'C:\Users\arouxsibilon\OneDrive - UCL\Rprojects\2022_RadApt_filterednoise\...experiment')

print("Current working directory: {0}".format(os.getcwd()))
cwd = format(os.getcwd())

stimdir = cwd + '\stim\\' #directory where the stimuli are
datadir = cwd + '\data\\' #directory to save data in


#%%#
'''
Open dlg box, Store info about the experiment session
'''

# Get subject's info through a dialog box
exp_name = 'Radapt_baselineRB_filterednoise'
exp_info = {
    'subj_ID': '',
    'session':'',
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

# Number of trials that we want for each condition (e.g., condition [VF = left, orientation = horizontal])
nTrialsPerStaircase = 100

# max time (in s) to wait for a response
timelimit = 10 

# Number of instructions slides
NBinstructions = list(range(4))

# size of instructions images
instrWIDTH = 1600
instrHEIGHT = 900

# fixation color
neutralColor = (-1, -1, -1)
waitColor = (-0.2, -0.2, -0.2) #for when waiting for a response
OKcolor = (-1, 1, -1) #green
notOKcolor = (1, -1, -1) #red

# size of the gaussian background
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
'''

#%%#  Experimental design
eccentricity = ['15dva']
meridians = ['meridianH','meridianV']
Hsides = ['left','right']
Vsides = ['up','down']
patchOrientations = ['oriH','oriV']

# Create the trial list:
# VF*4 (left, right, up, down)
# ori*2 (oriH, oriV)
# patch*10 (1 .... 10)
triallist = [{'VF':'left','ori':'oriH','patch':0},
              {'VF':'left','ori':'oriV','patch':0},
              {'VF':'right','ori':'oriH','patch':0},
              {'VF':'right','ori':'oriV','patch':0},
              {'VF':'up','ori':'oriH','patch':0},
              {'VF':'up','ori':'oriV','patch':0},
              {'VF':'down','ori':'oriH','patch':0},
              {'VF':'down','ori':'oriV','patch':0},
              {'VF':'left','ori':'oriH','patch':1},
              {'VF':'left','ori':'oriV','patch':1},
              {'VF':'right','ori':'oriH','patch':1},
              {'VF':'right','ori':'oriV','patch':1},
              {'VF':'up','ori':'oriH','patch':1},
              {'VF':'up','ori':'oriV','patch':1},
              {'VF':'down','ori':'oriH','patch':1},
              {'VF':'down','ori':'oriV','patch':1},
              {'VF':'left','ori':'oriH','patch':2},
              {'VF':'left','ori':'oriV','patch':2},
              {'VF':'right','ori':'oriH','patch':2},
              {'VF':'right','ori':'oriV','patch':2},
              {'VF':'up','ori':'oriH','patch':2},
              {'VF':'up','ori':'oriV','patch':2},
              {'VF':'down','ori':'oriH','patch':2},
              {'VF':'down','ori':'oriV','patch':2},
              {'VF':'left','ori':'oriH','patch':3},
              {'VF':'left','ori':'oriV','patch':3},
              {'VF':'right','ori':'oriH','patch':3},
              {'VF':'right','ori':'oriV','patch':3},
              {'VF':'up','ori':'oriH','patch':3},
              {'VF':'up','ori':'oriV','patch':3},
              {'VF':'down','ori':'oriH','patch':3},
              {'VF':'down','ori':'oriV','patch':3},
              {'VF':'left','ori':'oriH','patch':4},
              {'VF':'left','ori':'oriV','patch':4},
              {'VF':'right','ori':'oriH','patch':4},
              {'VF':'right','ori':'oriV','patch':4},
              {'VF':'up','ori':'oriH','patch':4},
              {'VF':'up','ori':'oriV','patch':4},
              {'VF':'down','ori':'oriH','patch':4},
              {'VF':'down','ori':'oriV','patch':4},
              {'VF':'left','ori':'oriH','patch':5},
              {'VF':'left','ori':'oriV','patch':5},
              {'VF':'right','ori':'oriH','patch':5},
              {'VF':'right','ori':'oriV','patch':5},
              {'VF':'up','ori':'oriH','patch':5},
              {'VF':'up','ori':'oriV','patch':5},
              {'VF':'down','ori':'oriH','patch':5},
              {'VF':'down','ori':'oriV','patch':5},
              {'VF':'left','ori':'oriH','patch':6},
              {'VF':'left','ori':'oriV','patch':6},
              {'VF':'right','ori':'oriH','patch':6},
              {'VF':'right','ori':'oriV','patch':6},
              {'VF':'up','ori':'oriH','patch':6},
              {'VF':'up','ori':'oriV','patch':6},
              {'VF':'down','ori':'oriH','patch':6},
              {'VF':'down','ori':'oriV','patch':6},
              {'VF':'left','ori':'oriH','patch':7},
              {'VF':'left','ori':'oriV','patch':7},
              {'VF':'right','ori':'oriH','patch':7},
              {'VF':'right','ori':'oriV','patch':7},
              {'VF':'up','ori':'oriH','patch':7},
              {'VF':'up','ori':'oriV','patch':7},
              {'VF':'down','ori':'oriH','patch':7},
              {'VF':'down','ori':'oriV','patch':7},
              {'VF':'left','ori':'oriH','patch':8},
              {'VF':'left','ori':'oriV','patch':8},
              {'VF':'right','ori':'oriH','patch':8},
              {'VF':'right','ori':'oriV','patch':8},
              {'VF':'up','ori':'oriH','patch':8},
              {'VF':'up','ori':'oriV','patch':8},
              {'VF':'down','ori':'oriH','patch':8},
              {'VF':'down','ori':'oriV','patch':8},
              {'VF':'left','ori':'oriH','patch':9},
              {'VF':'left','ori':'oriV','patch':9},
              {'VF':'right','ori':'oriH','patch':9},
              {'VF':'right','ori':'oriV','patch':9},
              {'VF':'up','ori':'oriH','patch':9},
              {'VF':'up','ori':'oriV','patch':9},
              {'VF':'down','ori':'oriH','patch':9},
              {'VF':'down','ori':'oriV','patch':9}
              ]
  

# nb trials...
nStaircaise = int(len(triallist)/10)  
nTrialsTotal = nTrialsPerStaircase * nStaircaise


  
for i in range(int(nTrialsPerStaircase/10)-1):
    condition_template = [{'VF':'left','ori':'oriH','patch':0},
              {'VF':'left','ori':'oriV','patch':0},
              {'VF':'right','ori':'oriH','patch':0},
              {'VF':'right','ori':'oriV','patch':0},
              {'VF':'up','ori':'oriH','patch':0},
              {'VF':'up','ori':'oriV','patch':0},
              {'VF':'down','ori':'oriH','patch':0},
              {'VF':'down','ori':'oriV','patch':0},
              {'VF':'left','ori':'oriH','patch':1},
              {'VF':'left','ori':'oriV','patch':1},
              {'VF':'right','ori':'oriH','patch':1},
              {'VF':'right','ori':'oriV','patch':1},
              {'VF':'up','ori':'oriH','patch':1},
              {'VF':'up','ori':'oriV','patch':1},
              {'VF':'down','ori':'oriH','patch':1},
              {'VF':'down','ori':'oriV','patch':1},
              {'VF':'left','ori':'oriH','patch':2},
              {'VF':'left','ori':'oriV','patch':2},
              {'VF':'right','ori':'oriH','patch':2},
              {'VF':'right','ori':'oriV','patch':2},
              {'VF':'up','ori':'oriH','patch':2},
              {'VF':'up','ori':'oriV','patch':2},
              {'VF':'down','ori':'oriH','patch':2},
              {'VF':'down','ori':'oriV','patch':2},
              {'VF':'left','ori':'oriH','patch':3},
              {'VF':'left','ori':'oriV','patch':3},
              {'VF':'right','ori':'oriH','patch':3},
              {'VF':'right','ori':'oriV','patch':3},
              {'VF':'up','ori':'oriH','patch':3},
              {'VF':'up','ori':'oriV','patch':3},
              {'VF':'down','ori':'oriH','patch':3},
              {'VF':'down','ori':'oriV','patch':3},
              {'VF':'left','ori':'oriH','patch':4},
              {'VF':'left','ori':'oriV','patch':4},
              {'VF':'right','ori':'oriH','patch':4},
              {'VF':'right','ori':'oriV','patch':4},
              {'VF':'up','ori':'oriH','patch':4},
              {'VF':'up','ori':'oriV','patch':4},
              {'VF':'down','ori':'oriH','patch':4},
              {'VF':'down','ori':'oriV','patch':4},
              {'VF':'left','ori':'oriH','patch':5},
              {'VF':'left','ori':'oriV','patch':5},
              {'VF':'right','ori':'oriH','patch':5},
              {'VF':'right','ori':'oriV','patch':5},
              {'VF':'up','ori':'oriH','patch':5},
              {'VF':'up','ori':'oriV','patch':5},
              {'VF':'down','ori':'oriH','patch':5},
              {'VF':'down','ori':'oriV','patch':5},
              {'VF':'left','ori':'oriH','patch':6},
              {'VF':'left','ori':'oriV','patch':6},
              {'VF':'right','ori':'oriH','patch':6},
              {'VF':'right','ori':'oriV','patch':6},
              {'VF':'up','ori':'oriH','patch':6},
              {'VF':'up','ori':'oriV','patch':6},
              {'VF':'down','ori':'oriH','patch':6},
              {'VF':'down','ori':'oriV','patch':6},
              {'VF':'left','ori':'oriH','patch':7},
              {'VF':'left','ori':'oriV','patch':7},
              {'VF':'right','ori':'oriH','patch':7},
              {'VF':'right','ori':'oriV','patch':7},
              {'VF':'up','ori':'oriH','patch':7},
              {'VF':'up','ori':'oriV','patch':7},
              {'VF':'down','ori':'oriH','patch':7},
              {'VF':'down','ori':'oriV','patch':7},
              {'VF':'left','ori':'oriH','patch':8},
              {'VF':'left','ori':'oriV','patch':8},
              {'VF':'right','ori':'oriH','patch':8},
              {'VF':'right','ori':'oriV','patch':8},
              {'VF':'up','ori':'oriH','patch':8},
              {'VF':'up','ori':'oriV','patch':8},
              {'VF':'down','ori':'oriH','patch':8},
              {'VF':'down','ori':'oriV','patch':8},
              {'VF':'left','ori':'oriH','patch':9},
              {'VF':'left','ori':'oriV','patch':9},
              {'VF':'right','ori':'oriH','patch':9},
              {'VF':'right','ori':'oriV','patch':9},
              {'VF':'up','ori':'oriH','patch':9},
              {'VF':'up','ori':'oriV','patch':9},
              {'VF':'down','ori':'oriH','patch':9},
              {'VF':'down','ori':'oriV','patch':9}
              ]
    triallist.extend(condition_template)
random.shuffle(triallist)
len(triallist)
    

    
    
#%%#
'''
Prepare window object and stimuli
'''
# Window object
###############
OLED = monitors.Monitor('testMonitor') #on changera ça après avoir fait la calibration
OLED.setSizePix((3840, 2160)) 
win = visual.Window(monitor = OLED,
                    color = (-1, -1, -1),
                    units = 'pix',
                    fullscr = True,
                    allowGUI = False)
win.setMouseVisible(False)



# Fixation dot
##############
fix = np.ones((20, 20))*(-1)
fixation = visual.GratingStim(win, tex=fix, mask='gauss', units='pix', size=20      )    

# Instructions images
#####################
instructions = visual.ImageStim(win, units = 'pix',
                               pos = (0,0), size = (instrWIDTH,instrHEIGHT)) 

# 2 - Patch Stimuli
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
##################
bleepf = os.path.join(stimdir + 'blip.wav')
bleep = sound.Sound(value=bleepf) 


# Gaussian Gray background
##########################
gaussianGrayf = os.path.join(stimdir + 'gaussianGray.bmp') 
gaussianGray = visual.ImageStim(win, image = gaussianGrayf,
                                units = 'pix', pos = (0,0), 
                                size = (bgSize,bgSize))

# Pause text
############
pause = visual.TextStim(win, color = (-1, -1, -0.5))







#%%#
'''
Prepare staircases
'''


#  Define Staircase parameters
##############################

ndown = 2 # Nb of correct responses before decreasing the contrast
nup = 1 # Nb of incorrect responses before increasing the contrast
down_step = 0.02
up_step = 0.03
maxContrast = 0.05



# initializes some dictionaries used by the staircase() function
thisCond = [] 
contrast_dict = {
    'left_oriH': 0,
    'left_oriV': 0,
    'right_oriH': 0,
    'right_oriV': 0,
    'up_oriH': 0,
    'up_oriV': 0,
    'down_oriH': 0,
    'down_oriV': 0
    }
acc_count_dict = {
    'left_oriH': 0,
    'left_oriV': 0,
    'right_oriH': 0,
    'right_oriV': 0,
    'up_oriH': 0,
    'up_oriV': 0,
    'down_oriH': 0,
    'down_oriV': 0
    }
trial_count_dict = {
    'left_oriH': 0,
    'left_oriV': 0,
    'right_oriH': 0,
    'right_oriV': 0,
    'up_oriH': 0,
    'up_oriV': 0,
    'down_oriH': 0,
    'down_oriV': 0
    }


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
Instructions / Practice
'''



'''
TEST LOOP
'''





# Initialize output arrays

trainingtest_array = []
trial_array = []
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
patchsample_array = []

win.flip()




trial = 0

# Create ZH (='zeHigh') variables for the high contrasts trials    
ZH_left_oriH = 0
ZH_right_oriH = 0
ZH_up_oriH = 0
ZH_down_oriH = 0
ZH_left_oriV = 0
ZH_right_oriV = 0
ZH_up_oriV = 0
ZH_down_oriV = 0
    
    
for thisTrial in range(len(triallist)): 
    trial = trial + 1
    theTrial = triallist[thisTrial]
    theVF = theTrial['VF']
    theOri = theTrial['ori']
    thePatch = theTrial['patch']
    thisCond = theVF + '_' + theOri
    trial_count_dict[thisCond] = trial_count_dict[thisCond] + 1
    if (theVF == 'left') or (theVF == 'right'):
        theMeridian = "meridianH"
    else:
        theMeridian  = "meridianV"

    # Set patch sample
    patch.setImage(patchSamples[thePatch])
    
    # set patch position depending on the condition
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
    # either pick within higher contrast range
    if (trial_count_dict[thisCond]%5 == 0):

        if theOri == 'oriH':
            if theVF == 'left':
                zecontrast = highContrastLevels[ZH_left_oriH]
                ZH_left_oriH = ZH_left_oriH + 1
                patch.contrast = zecontrast    
            if theVF == 'right':
                zecontrast = highContrastLevels[ZH_right_oriH]
                ZH_right_oriH = ZH_right_oriH + 1
                patch.contrast = zecontrast
            if theVF == 'up':
                zecontrast = highContrastLevels[ZH_up_oriH]
                ZH_up_oriH = ZH_up_oriH + 1
                patch.contrast = zecontrast               
            if theVF == 'down':
                zecontrast = highContrastLevels[ZH_down_oriH]
                ZH_down_oriH = ZH_down_oriH + 1
                patch.contrast = zecontrast
        elif theOri == 'oriV':
            if theVF == 'left':
                zecontrast = highContrastLevels[ZH_left_oriV]
                ZH_left_oriV = ZH_left_oriV + 1
                patch.contrast = zecontrast    
            if theVF == 'right':
                zecontrast = highContrastLevels[ZH_right_oriV]
                ZH_right_oriV = ZH_right_oriV + 1
                patch.contrast = zecontrast
            if theVF == 'up':
                zecontrast = highContrastLevels[ZH_up_oriV]
                ZH_up_oriV = ZH_up_oriV + 1
                patch.contrast = zecontrast               
            if theVF == 'down':
                zecontrast = highContrastLevels[ZH_down_oriV]
                ZH_down_oriV = ZH_down_oriV + 1
                patch.contrast = zecontrast  
                
        contrast_array.append(zecontrast)
        contrastRule_array.append("highCont")  
    
    # or use staircase rules      
    else:
        staircase(thisCond)
        patch.contrast = abs(contrast_dict[thisCond])            
        contrast_array.append(contrast_dict[thisCond])
        contrastRule_array.append("staircase")




    ''' Draw stimuli on screen '''
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
    ptch = 'patch' + str(thePatch+1)
    trainingtest_array.append('test')
    trial_array.append(trial)
    eccentricity_array.append(eccentricity)
    xPos_array.append(xPos)
    yPos_array.append(yPos)
    meridian_array.append(theMeridian)
    patch_ori_array.append(theOri)
    VF_array.append(theVF)
    patchsample_array.append(ptch)
    resp_array.append(resp)
    accuracy_array.append(acc)
    accCount_array.append(acc_count_dict[thisCond])
    thisCond_array.append(thisCond)
    trialCount_array.append(trial_count_dict[thisCond])


    ''' Should we make a small break? ''' 
    if (trial%25 == 0):
        # PAUSE
        progression = thisTrial*100/nTrialsTotal
        pause_txt = 'Take a little break : ) \n progression' + str(progression) + '%' + '\n \n Press SPACE to resume'
        pause.setText(pause_txt)
        gaussianGray.draw()
        pause.draw()
        win.flip() 
        event.clearEvents()
        keys = event.waitKeys(keyList=['space', 'q'])
        if 'q' in keys:
            win.close()
            core.quit()
        if 'space' in keys:
            gaussianGray.draw()
            win.flip()
            core.wait(2)







#%%#
'''
Save data and pickle some objects for the next session
'''
win.close()


if not os.path.isdir(datadir):
    os.makedirs(datadir)
data_fname = exp_name + '_' + exp_info['subj_ID']+ '_session'+ exp_info['session'] + '_' + exp_info['date'] + '.csv'
data_fname = os.path.join(datadir, data_fname)

subj_ID = exp_info['subj_ID']
exp_date = exp_info['date']


actualNtrials = len(contrastRule_array)

subject_array = []
exp_name_array = []
date_array = [] 
session_array = []
patchSize_array = []
patchSizeDVA_array = []
patchSFDVA_array = []
for n in range(actualNtrials):
    subject_array.append(subj_ID)
    exp_name_array.append(exp_name)
    date_array.append(exp_info['date'])
    session_array.append(exp_info['session'])
    patchSize_array.append(patchSize)
    patchSizeDVA_array.append(patchSizeDVA)
    
    

output_file = pd.DataFrame({'subj_ID': subject_array,
                            'exp_name': exp_name_array,
                            'date': date_array,
                            'session': session_array,
                            'training-test': trainingtest_array,
                            'trial': trial_array,
                            'eccentricity': eccentricity_array,
                            'xPosition': xPos_array,
                            'yPosition': yPos_array,
                            'meridian': meridian_array,
                            'contrast': contrast_array,
                            'ori': patch_ori_array,
                            'VF': VF_array,
                            'resp': resp_array,
                            'accuracy': accuracy_array,
                            'accCount': accCount_array,
                            'condition': thisCond_array,
                            'trialCount': trialCount_array,
                            'contrastRule': contrastRule_array
                            })

# save the csv file + pickle

# CSV file
output_file.to_csv(data_fname, index = False)

# Pickle
# with open(data_fname + ".pkl", 'wb') as f:
#     pickle.dump(output_file, f, pickle.HIGHEST_PROTOCOL)
print('FILES SAVED')


win.close()
