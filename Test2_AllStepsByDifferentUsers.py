# ============================================================================
# COPYRIGHT: Copyright (c) 2010, Mark Gilkey.  All rights reserved.  
# PURPOSE: This is test for ParallAssist.
#     This tests a simple case where all the steps are to be executed by 
#     the same stepper.  
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
           pStatement = "print('Greetings, earthlings.')",
           pLanguage = "PythonExec",
           pTimeLimit = 1,
           pExpectedResult = None, 
           pLanguageSupportObject = lsoPythonExec,
           pParallel = False)
stepList.append(step)


step = StepClass(pStepNum = 1,
           pStepperNum = 2,
           pStatement = "print('Greetings, moonlings.')",
           pLanguage = "PythonExec",
           pTimeLimit = 1,
           pExpectedResult = None, 
           pLanguageSupportObject = lsoPythonExec,
           pParallel = False)
stepList.append(step)


step = StepClass(pStepNum = 2,
           pStepperNum = 3,
           pStatement = "print('This planet is not civilized.')",
           pLanguage = "PythonExec",
           pTimeLimit = 1,
           pExpectedResult = None, 
           pLanguageSupportObject = lsoPythonExec,
           pParallel = False)
stepList.append(step)
