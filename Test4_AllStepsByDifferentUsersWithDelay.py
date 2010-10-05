# ============================================================================
# COPYRIGHT: Copyright (c) 2010, Mark Gilkey.  All rights reserved.  
# PURPOSE: This is test for ParallAssist.
#     This tests that we "wait" when we should (i.e. when the previous thread 
#     has not yet finished.  
#     WARNING: Currently this does not actually check that the "sleep" 
#     commands are respected; the expected and actual output will match 
#     even if the timing is wrong.  
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
           pStepperNum = 1,
           pStatement = 
            "import time; print('Sleeping...');time.sleep(5); print('Greetings, earthlings.')",
           pLanguage = "PythonExec",
           pTimeLimit = 6,
           pExpectedResult = None, 
           pLanguageSupportObject = lsoPythonExec,
           pParallel = False)
stepList.append(step)


step = StepClass(pStepNum = 1,
           pStepperNum = 2,
           pStatement = "import time\nprint('Sleeping more...')\ntime.sleep(10)\nprint('Greetings, moonlings.')",
           pLanguage = "PythonExec",
           pTimeLimit = 11,
           pExpectedResult = None, 
           pLanguageSupportObject = lsoPythonExec,
           pParallel = False)
stepList.append(step)


step = StepClass(pStepNum = 2,
           pStepperNum = 3,
           pStatement = "import time\nprint('Sleeping still more...')\ntime.sleep(10)\nprint('Greetings, Martians.')",
           pLanguage = "PythonExec",
           pTimeLimit = 11,
           pExpectedResult = None, 
           pLanguageSupportObject = lsoPythonExec,
           pParallel = False)
stepList.append(step)


step = StepClass(pStepNum = 3,
           pStepperNum = 4,
           pStatement = "print('This planet is not civilized.')",
           pLanguage = "PythonExec",
           pTimeLimit = 1,
           pExpectedResult = None, 
           pLanguageSupportObject = lsoPythonExec,
           pParallel = False)
stepList.append(step)
