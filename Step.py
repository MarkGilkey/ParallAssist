# ============================================================================
# COPYRIGHT: Copyright (c) 2010, Mark Gilkey.  All rights reserved.  
# PURPOSE: Represents a "step" in a list of steps.
# AUTHOR: mgilkey
# LAST MODIFIED:
#     2010-09-xx mgilkey
#         Added pre and post so that we can execute some code immediately 
#         before or immediately after executing the body of the step.  
#     2010-07-31 mgilkey
#        Added "Comment" field and related code.
#        Fleshed out the displaySelf() method.  
#        Added comments.
# LAST CODE REVIEW:
#     2010-07-31 mgilkey
# ============================================================================


"""PURPOSE: Represents a "step" in a list of steps.

This class represents a single "step", which is a sequence of 0 or 
more executable statements in any of the supported programming languages 
(including Python and Perl, and hopefully eventually including SQL, unix bash 
shell, etc.).

GUIDELINES:
1) Step numbers (stepNums) should be numbered 1 - N.  
2) Stepper numbers (stepperNums) should be numbered 1 - N.  
3) Every language must have a corresponding LanguageSupport class (defined 
   in a separate file).
"""


import time


import Runnable


from LanguageSupportPythonExec import LanguageSupportPythonExecClass


languageSupportObjectPythonExec1 = LanguageSupportPythonExecClass()


class StepClass (Runnable.RunnableClass):

    def __init__(self, 
     pStepNum,    # The step number (0 - N).
     pStepperNum, # Which user/connection should execute this statement.
     pStatement,  # The statement(s) to execute.
     pLanguage,   # Language in which the statement is written (e.g. Python).
     pTimeLimit,  # This is the maximum length of time that the step is 
                  # expected to run.  After this, we'll start the subsequent
                  # step even if this step hasn't completed.  
     pExpectedResult,  # The expected result.  See "Result" class.
     pLanguageSupportObject,  # The Language Support Object for this pLanguage
     pParallel = False,   # Run in parallel with previous step (as opposed to 
                  # sequentially (after prev step completes).  
                  # NOT SUPPORTED YET.
     pComment = "",  # Optional comment
     pPreStep = None, 
     pPostStep = None,
     pStepList = None,  # "Points to" the list of steps that this step is in.
     ):

        """PURPOSE: initialize a step object with step number, statement, etc.

        PARAMETERS:
         pStepNum,    # The step number (0 - N).
         pStepperNum, # An integer that indicates which user/connection should 
                      # execute this statement.  Usually 0-N (or 1-N), but 
                      # you may be able to use any unique integer to identify 
                      # a stepper.
         pStatement,  # The statement(s) to execute.
         pLanguage,   # Language in which the statement is written (e.g. PythonExec).
         pTimeLimit,  # This is the maximum length of time that the step is 
                      # expected to run.  After this, we'll start the subsequent
                      # step even if this step hasn't completed.  
         pExpectedResult,  # The expected result.  (See "Result" class.?!!!)
         pLanguageSupportObject,  # The Language Support Object for this pLanguage
         pParallel = False,   # Run in parallel with previous step (as opposed to 
                      # sequentially (after prev step completes).  
                      # NOT SUPPORTED YET.
         pComment = '.',  # Optional comment that may help debugging.
         pPreStep = None,   # Code to execute immediately before this step.
         pPostStep = None,  # Code to execute immediately after this step.
          pStepList = None,   # "Points to" the list of steps that this step is in.
         ):
    
        """

        self.stepNum = pStepNum
        self.stepperNum = pStepperNum
        self.statement = pStatement
        self.language = pLanguage
        self.timeLimit = pTimeLimit
        self.expectedResult = pExpectedResult
        self.languageSupportObject = pLanguageSupportObject
        self.parallel = pParallel
        self.comment = pComment
        self.stepList = pStepList

        self.actualResult = None  # This is the actual result of executing 
                             # the statement.  

        self.startTime = None   # The time that the step started executing.
                           # This helps us determine whether the step has 
                           # exceeded its time limit.
        self.endTime = None     # The time that the step finished executing.
                           # This is sometimes useful in debugging.

        self.preStep = pPreStep     # An optional step (sub-tree of steps?) to 
                           # execute immediately prior to this one (as part of 
                           # this step).   NOT YET SUPPORTED!!! This is an 
                           # advanced feature for the future...
        self.postStep = pPostStep    # An optional step (sub-tree of steps?) to 
                           # execute immediately after this one (as part of this 
                           # step).   NOT YET SUPPORTED!!!


    def runMe(self, pPfx):
        pfx = pPfx + self.__class__.__name__ + ": runMe(): "

        self.startTime = time.time()

        # To allow the preStep and postStep of one step to access the actual 
        # results of another step, the eval() function that is executing the 
        # the preExecute or postExecute needs to be able to access the 
        # stepList (the list that contains all the steps).  But when I call a 
        # languageSupportObject.executeStatementAndReturnValue() method, 
        # that method calls the eval() function, but eval() doesn't know 
        # about the stepList.  To solve this, I add a field to each step to 
        # point to the stepList, 
        # and I create a local variable named "ThisStep" that points to this 
        # step (and thus indirectly to the stepList) and I 
        # pass the local variables (returned by the locals() function) and 
        # tell the eval() function to use those local variable.  This works, 
        # but it feels inelegant and I wonder if there is a better way.  
        ThisStep = self     # Point to this step
        dictionaryOfLocalVariables = locals()

        if self.preStep != None and self.preStep != "":
            languageSupportObjectPythonExec1.executeStatementAndReturnValue(
             self.preStep, dictionaryOfLocalVariables)

        rv = self.languageSupportObject.executeStatementAndReturnValue(
             self.statement, dictionaryOfLocalVariables)
        self.actualResult = rv

        if self.postStep != None and self.postStep != "":
            languageSupportObjectPythonExec1.executeStatementAndReturnValue(
             self.postStep, dictionaryOfLocalVariables)

        self.endTime = time.time()
        

    def displayMe(self):
        """
        PURPOSE: Return string containing object contents for debugging.
        """

        h = ""
        h += str(self.stepNum) + '\n'
        h += str(self.stepperNum) + '\n'
        h += str(self.statement) + '\n'
        h += str(self.language) + '\n'
        h += str(self.startTime) + '\n'
        h += str(self.endTime) + '\n'
        if self.endTime != None and self.startTime != None:
            h += str(self.endTime - self.startTime) + '\n'
        else:
            h += '(Not available)' + '\n'
        h += str(self.timeLimit) + '\n'
        h += str(self.expectedResult) + '\n'
        h += str(self.actualResult) + '\n'
        if self.comment != None and self.comment != "": 
            h += str(self.comment) + '\n'
        print(h)
        return h


    def returnMeAsHtml(self):
        """PURPOSE: Return info about the step as a row of HTML."""

        h = '<tr>'

        h += '<td>' + str(self.stepNum) + '</td>'
        h += '<td>' + str(self.stepperNum) + '</td>'
        h += '<td>' + str(self.statement) + '</td>'
        h += '<td>' + str(self.language) + '</td>'
        h += '<td>' + str(self.startTime) + '</td>'
        h += '<td>' + str(self.endTime) + '</td>'
        if self.endTime != None and self.startTime != None:
            h += '<td>' + str(self.endTime - self.startTime) + '</td>'
        else:
            h += '<td>' + '(Not available)' + '</td>'
        h += '<td>' + str(self.timeLimit) + '</td>'
        h += '<td>' + str(self.expectedResult) + '</td>'
        if self.actualResult == self.expectedResult:
            startColor = '<span style="color: rgb(0, 200, 0);">'
        else:
            startColor = '<span style="color: rgb(255, 0, 0);">'
        endColor = '</span>'
        h += '<td>' + startColor + str(self.actualResult) + endColor + '</td>'
        h += '<td>' + str(self.comment) + '</td>'
        h += '</tr>'

        return h


    def returnHeaderAsHtml():
        """PURPOSE: Return a "header" for the HTML table."""

        h = '<tr>'

        h += '<td><b>' + "Step Number" + '</b></td>'
        h += '<td><b>' + "Stepper Number" + '</b></td>'
        h += '<td><b>' + "Statement" + '</b></td>'
        h += '<td><b>' + "Language" + '</b></td>'
        h += '<td><b>' + "StartTime" + '</b></td>'
        h += '<td><b>' + "EndTime" + '</b></td>'
        h += '<td><b>' + "Execution Time" + '</b></td>'
        h += '<td><b>' + "Timeout" + '</b></td>'
        h += '<td><b>' + "Expected Result" + '</b></td>'
        h += '<td><b>' + "Actual Result" + '</b></td>'
        h += '<td><b>' + "Comment" + '</b></td>'
#        h += '<td><b>' +  + '</b></td>'

        h += '</tr>'

        return h


    # Tell Python that it's ok to call returnHeaderAsHtml even if 
    # you haven't instantiated an object in this class.
    returnHeaderAsHtml=staticmethod(returnHeaderAsHtml)
