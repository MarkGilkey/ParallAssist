# ============================================================================
# COPYRIGHT: Copyright (c) 2010, Mark Gilkey.  All rights reserved.  
# PURPOSE: This sample code demonstrates how to create a step list in which 
#     some steps refer to the results of other steps.  Specifically, in this 
#     case, step 1 modifies step2's command to take into account the result 
#     of step 0.
# AUTHOR: mgilkey
# LAST MODIFIED:
# 
# ============================================================================


# --- Import language support objects for each language that we want to use.
from LanguageSupportPythonExec import LanguageSupportPythonExecClass
from LanguageSupportPythonEval import LanguageSupportPythonEvalClass
from LanguageSupportPerl import LanguageSupportPerlClass


# --- Create language support objects (LSOs) for each language.
# Note that in the future we might support having multiple language support 
# objects for the same language if different steppers or different steps 
# need independent LSOs.
lsoPythonExec = LanguageSupportPythonExecClass(pContext = None)
lsoPythonEval = LanguageSupportPythonEvalClass(pContext = None)
lsoPerl = LanguageSupportPerlClass(pContext = None)


# --- Create the list of steps.
from Step import StepClass

stepList = []

step = StepClass(pStepNum = 0,
           pStepperNum = 0,
           pStatement = "print 'Hello, perled\n'; $x = 18; print $x + '\n';",
           pLanguage = "Perl",
           pTimeLimit = 1,
           pExpectedResult = ['Hello, perled\n', '18'], 
           pLanguageSupportObject = lsoPerl,
           pParallel = False)
stepList.append(step)


# The statement refers to the result of an earlier step.
step = StepClass(pStepNum = 1,
           pStepperNum = 0,
           pStatement = "print('This step just modifies step 2.')",
           pLanguage = "PythonEval",
           pTimeLimit = 1,
           pExpectedResult = 'RESULT of step 0 was: 18', 
           pParallel = False,
           pLanguageSupportObject = lsoPythonEval,
           pComment = "Try to 'read' the result of an earlier step.",
           pPreStep = "print('Hello from preStep')",
           pPostStep = "ThisStep.stepList[2].statement = ThisStep.stepList[2].statement % (ThisStep.stepList[0].actualResult[1])",
           pStepList = stepList)
stepList.append(step)

# The preStep actually updates the statement to be executed so that the  
# statement contains the result of an earlier step.  
# This technique allows you to dynamically compose statements that contain 
# a user id, query result, etc.  
step = StepClass(pStepNum = 2,
           pStepperNum = 0,
           pStatement = "print('RESULT of step 0 was: %s.')",
           pLanguage = "PythonEval",
           pTimeLimit = 1,
           pExpectedResult = ['Substitution: 18'], 
           pParallel = False,
           pLanguageSupportObject = lsoPerl,
           pComment = "Try to use the result of an earlier step.",
           pStepList = stepList)
stepList.append(step)
