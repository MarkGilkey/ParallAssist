# ============================================================================
# COPYRIGHT: Copyright (c) 2010, Mark Gilkey.  All rights reserved.  
# PURPOSE: Use this sample code as a model for creating a step list.
# AUTHOR: mgilkey
# LAST MODIFIED:
# 
# ============================================================================


# --- Import language support objects for each language that we want to use.
from LanguageSupportPythonExec import LanguageSupportPythonExecClass


# --- Create language support objects (LSOs) for each language.
lsoPythonExec = LanguageSupportPythonExecClass(pContext = None)


# --- Create list of steps to execute.
from Step import StepClass

stepList = []

step = StepClass(pStepNum = 0,
           pStepperNum = 0,
           pStatement = "print('Greetings, earthlings!')",
           pLanguage = "PythonExec",
           pTimeLimit = 1,
           pExpectedResult = None, 
           pLanguageSupportObject = lsoPythonExec,
           pParallel = False)
stepList.append(step)


step = StepClass(pStepNum = 1,
           pStepperNum = 0,
           pStatement = "print('Greetings, moonlings!')",
           pLanguage = "PythonExec",
           pTimeLimit = 1,
           pExpectedResult = None, 
           pLanguageSupportObject = lsoPythonExec,
           pParallel = False)
stepList.append(step)
