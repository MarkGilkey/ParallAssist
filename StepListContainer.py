# ============================================================================
# COPYRIGHT: Copyright (c) 2010, Mark Gilkey.  All rights reserved.
# PURPOSE:
#     This contains a list of steps and a list of log objects.  
# AUTHOR: mgilkey
# LAST CODE REVIEW:
#     2010-07-31 mgilkey
# ============================================================================



import errCodes

import HTMLShortCuts

import Step


class StepListContainerClass():

    """PURPOSE: This contains a list of steps and related info.

        The related info includes:
            the step number of the most recently completed step.
    """

    def __init__(self, pPfx, pLogObjectContainer, pListOfSteps = []):

        """PURPOSE: Create a log object container to hold 1 or more "logs".

        PARAMETERS:
            pPfx: A string that may contain useful diagnostic information.
               Typically, this contains the name of the calling function, 
               the caller's caller, etc.
            pLogObjectContainer: This contains info that helps us write info 
               to log file(s).
            pListOfSteps: A list of StepClass objects to execute.  
        """

        pfx = pPfx + "StepListContainerClass.__init__(): "
        msg = "DDDDIAGNOSTIC: " + pfx
        pLogObjectContainer.logMsg(pfx, msg, errCodes.ES_Info)
#        print(pListOfSteps)

        self.logObjectContainer = pLogObjectContainer
        self.listOfSteps = pListOfSteps
#        print("DDDIAGNOSTIC: ", pfx, "self.listOfSteps = ", self.listOfSteps)

        # Step numbers start from zero, and at the beginning the most recent 
        # step completed should be one less than the first step, so initially 
        # we set the "last step completed" to -1.  
        self.lastStepNumCompleted = -1
        self.numSteps = len(self.listOfSteps)


    def appendStep(self, pStep):
        self.listOfSteps.append(pStep)


    def displayMe(self):
        for s in self.listOfSteps:
            s.displayMe()


    def returnMeAsHtml(self):
        """PURPOSE: Create a string that holds the step list in HTML."""

        h = HTMLShortCuts.startDoc
        h += HTMLShortCuts.startTableBody
        h += Step.StepClass.returnHeaderAsHtml()
        for step in self.listOfSteps:
            h += step.returnMeAsHtml()
        h += HTMLShortCuts.endTableBody
        h += HTMLShortCuts.endDoc
        return h

