# ============================================================================
# COPYRIGHT: Copyright (c) 2010, Mark Gilkey.  All rights reserved.  
# PURPOSE: This is a test for ParallAssist.
#     This tests that we recognize when return values 
#     do or do not match.  Note that the expected output in the 2nd 
#     statement is deliberately wrong.  This test should "fail", i.e. 
#     it should complain that the actual and expected values did not match!
# AUTHOR: mgilkey
# LAST MODIFIED:
# 
# ============================================================================


# --- Import language support objects for each language that we want to use.
from LanguageSupportPythonEval import LanguageSupportPythonEvalClass


# --- Create language support objects (LSOs) for each language.
lsoPythonEval = LanguageSupportPythonEvalClass(pContext = None)


# --- Create the list of steps.
from Step import StepClass

stepList = []

step = StepClass(pStepNum = 0,
           pStepperNum = 0,
           pStatement = "'This should match'",
           pLanguage = "PythonEval",
           pTimeLimit = 2,
           pExpectedResult = "This should match", 
           pLanguageSupportObject = lsoPythonEval,
           pParallel = False)
stepList.append(step)


step = StepClass(pStepNum = 1,
           pStepperNum = 1,
           pStatement = 
            "'This is not going to match.'",
           pLanguage = "PythonEval",
           pTimeLimit = 3,
           pExpectedResult = "This is not the same!", 
           pComment = 
            "This SHOULD fail because actual and expected results do not match.",
           pLanguageSupportObject = lsoPythonEval,
           pParallel = False)
stepList.append(step)


