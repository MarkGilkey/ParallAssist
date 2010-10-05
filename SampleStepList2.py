# ============================================================================
# COPYRIGHT: Copyright (c) 2010, Mark Gilkey.  All rights reserved.  
# PURPOSE: This sample code demonstrates the use of multiple languages; this
#     uses perl statements as well as Python statements.  
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
           pStatement = "print('Greetings, earthlings.')",
           pLanguage = "PythonExec",
           pTimeLimit = 1,
           pExpectedResult = None, 
           pLanguageSupportObject = lsoPythonExec,
           pParallel = False)
stepList.append(step)


step = StepClass(pStepNum = 1,
           pStepperNum = 0,
           pStatement = "print('Greetings, moonlings.')",
           pLanguage = "PythonExec",
           pTimeLimit = 1,
           pExpectedResult = None, 
           pLanguageSupportObject = lsoPythonExec,
           pParallel = False)
stepList.append(step)


step = StepClass(pStepNum = 2,
           pStepperNum = 0,
           pStatement = "print 'Hello, perled\n'; $x = 18; print $x + '\n';",
           pLanguage = "Perl",
           pTimeLimit = 1,
           pExpectedResult = ['Hello, perled\n', '18'], 
           pLanguageSupportObject = lsoPerl,
           pParallel = False)
stepList.append(step)

