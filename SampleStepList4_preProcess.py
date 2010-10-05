# ============================================================================
# COPYRIGHT: Copyright (c) 2010, Mark Gilkey.  All rights reserved.  
# PURPOSE: This sample code demonstrates how to create a step list in which 
#     some steps refer to the results of other steps.   Specifically, in this 
#     case, a preStep in step 2 uses the result of step 0. 
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
           pStatement = "'RESULT of step 0 was: ' + str(ThisStep.stepList[0].actualResult[1])",
           pLanguage = "PythonEval",
           pTimeLimit = 1,
           pExpectedResult = 'RESULT of step 0 was: 18', 
           pParallel = False,
           pLanguageSupportObject = lsoPythonEval,
           pComment = "Try to 'read' the result of an earlier step.",
           pStepList = stepList)
stepList.append(step)

# The preStep actually updates the statement to be executed so that the  
# statement contains the result of an earlier step.  
# This technique allows you to dynamically compose statements that contain 
# a user id, query result, etc.  
step = StepClass(pStepNum = 2,
           pStepperNum = 0,
           pStatement = "print('Substitution: %s');",
           pLanguage = "Perl",
           pTimeLimit = 1,
           pExpectedResult = ['Substitution: 18'], 
           pParallel = False,
           pLanguageSupportObject = lsoPerl,
           pComment = "Try to 'read' the result of an earlier step.",
           pPreStep = "ThisStep.statement = ThisStep.statement % (ThisStep.stepList[0].actualResult[1])",
           pPostStep = "print('Hello from postStep')",
           pStepList = stepList)
stepList.append(step)


# ---------------- Set the language support objects...
#    Ideally, the user would not need to create the language support 
#    objects; we could do that for him based on the pLanguage values 
#    that he sets in each step.  We might be able to modify the code 
#    below to create the language support objects and set the 
#    pLanguageSupport value for each step!!!

#        # Get a list of all of the LanguageSupportObjects we will need.
#        listOfLanguages = []
#        for step in self.stepListContainerObject.listOfSteps:
#            if not listContainsElement(listOfLanguages, step.language):
#                listOfLanguages.append(step.language)
#
#        listOfLSOs = []
#        for lang in listOfLanguages:
#            lso_name = "LanguageSupport" + lang
#            cmd = "from " + lso_name + " import " + lso_name + "Class"
#            print("DDDIAGNOSTIC: cmd = " + cmd)
#            exec(cmd)
#            cmd = lso_name + "Class(pfx)"
#            print("DDDIAGNOSTIC: cmd = " + cmd)
#            lso = eval(cmd)
#                # Will this actually set the "lso" variable?
#                # Do I need "eval()" rather than "exec()"??!!!
#            listOfLSOs.append(lso)
#        lsoContainer1 = LanguageSupportObjectContainerClass(pfx, 
#         self.logObjectContainer, listOfLSOs)

