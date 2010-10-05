# ============================================================================
# COPYRIGHT: Copyright (c) 2010, Mark Gilkey.  All rights reserved.  
# PURPOSE: This is test for ParallAssist.
#     This tests that we run correctly when stepper numbers start at 0 
#     rather than at 1.  (Most of my tests and demos start the stepper numbers 
#     at 1 and the step numbers at 0, which just means there's one unnecessary 
#     extra rule for people to remember.  It would be nice if you could start 
#     the stepper numbers from either 0 or 1.)
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
           pStepperNum = 0,
           pStatement = 
            "import time; print('Sleeping...');time.sleep(2); print('Step0.')",
           pLanguage = "PythonExec",
           pTimeLimit = 3,
           pExpectedResult = None, 
           pLanguageSupportObject = lsoPythonExec,
           pParallel = False)
stepList.append(step)


step = StepClass(pStepNum = 1,
           pStepperNum = 1,
           pStatement = 
            "import time\nprint('Sleeping...')\ntime.sleep(2)\nprint('Step1.')",
           pLanguage = "PythonExec",
           pTimeLimit = 3,
           pExpectedResult = None, 
           pLanguageSupportObject = lsoPythonExec,
           pParallel = False)
stepList.append(step)


step = StepClass(pStepNum = 2,
           pStepperNum = 2,
           pStatement = 
            "import time\nprint('Sleeping...')\ntime.sleep(2)\nprint('Step2.')",
           pLanguage = "PythonExec",
           pTimeLimit = 3,
           pExpectedResult = None, 
           pLanguageSupportObject = lsoPythonExec,
           pParallel = False)
stepList.append(step)


step = StepClass(pStepNum = 3,
           pStepperNum = 3,
           pStatement = 
            "import time\nprint('Sleeping...')\ntime.sleep(2)\nprint('Step3.')",
           pLanguage = "PythonExec",
           pTimeLimit = 3,
           pExpectedResult = None, 
           pLanguageSupportObject = lsoPythonExec,
           pParallel = False)
stepList.append(step)
