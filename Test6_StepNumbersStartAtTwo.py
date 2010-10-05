# ============================================================================
# COPYRIGHT: Copyright (c) 2010, Mark Gilkey.  All rights reserved.  
# PURPOSE: This is test for ParallAssist.
#     This tests that we run correctly when stepper numbers start at 2 
#     rather than at 1, and when they increase by more than one.  
#     I don't think it should matter what the stepper numbers start at; 
#     I don't think I ever use them to index into a list.  I think as long as 
#     the values are distinct, we should be ok.  Nonetheless, I recommend 
#     that they start at 0 or 1 and increment by 1.  
# AUTHOR: mgilkey
# LAST MODIFIED:
# 
# ============================================================================


# --- Import language support objects for each language that we want to use.
from LanguageSupportPythonExec import LanguageSupportPythonExecClass


# --- Create language support objects (LSOs) for each language.
lsoPythonExec = LanguageSupportPythonExecClass(pContext = None)


# --- Create the list of steps.
from Step import StepClass

stepList = []

step = StepClass(pStepNum = 0,
           pStepperNum = 2,
           pStatement = 
            "import time; print('Sleeping...');time.sleep(2); print('Step0.')",
           pLanguage = "PythonExec",
           pTimeLimit = 3,
           pExpectedResult = None, 
           pLanguageSupportObject = lsoPythonExec,
           pParallel = False)
stepList.append(step)


step = StepClass(pStepNum = 1,
           pStepperNum = 4,
           pStatement = 
            "import time\nprint('Sleeping...')\ntime.sleep(2)\nprint('Step1.')",
           pLanguage = "PythonExec",
           pTimeLimit = 3,
           pExpectedResult = None, 
           pLanguageSupportObject = lsoPythonExec,
           pParallel = False)
stepList.append(step)


step = StepClass(pStepNum = 2,
           pStepperNum = 5,
           pStatement = 
            "import time\nprint('Sleeping...')\ntime.sleep(2)\nprint('Step2.')",
           pLanguage = "PythonExec",
           pTimeLimit = 3,
           pExpectedResult = None, 
           pLanguageSupportObject = lsoPythonExec,
           pParallel = False)
stepList.append(step)


step = StepClass(pStepNum = 3,
           pStepperNum = 7,
           pStatement = 
            "import time\nprint('Sleeping...')\ntime.sleep(2)\nprint('Step3.')",
           pLanguage = "PythonExec",
           pTimeLimit = 3,
           pExpectedResult = None, 
           pLanguageSupportObject = lsoPythonExec,
           pParallel = False)
stepList.append(step)
