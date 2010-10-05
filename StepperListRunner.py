# ============================================================================
# COPYRIGHT: Copyright (c) 2010, Mark Gilkey.  All rights reserved.  
# PURPOSE: This creates a list of steppers and calls the runMe() method
#     for each of those steppers.
# AUTHOR: mgilkey
# LAST MODIFIED:
#     2010-10-01 mgilkey
#         Minor improvements to comments.  
# REVIEWED:
#     2010-10-01 mgilkey
# ============================================================================


"""
   PURPOSE: This creates a list of steppers and calls the runMe() method
      for each of those steppers.
"""


import Runnable
from RunParallel import * 
from Stepper import StepperClass



class StepperListRunnerClass(Runnable.RunnableClass):

    def __init__(self, pPfx, pLogObjectContainer, pStepListContainerObject,
     pStepListFileName):
        """
        PARAMETERS:
            pPfx: This contains a string useful in debugging, typically the 
                name of the calling function, the caller's caller, etc.
            pLogObjectContainer: this contains a list of object that can log 
                error and diagnostic messages.
            pStepListContainerObject: This contains the list of steps to execute.
        """
        self.logObjectContainer = pLogObjectContainer
        self.stepListContainerObject = pStepListContainerObject
        self.stepListFileName = pStepListFileName


    def createListOfSteppers(self, pPfx):

        """
        PURPOSE: Check the list of steps to find all the distinct stepper 
            numbers, and create a list of steppers (one for each stepper 
            number).
        """

        pfx = pPfx + "createListOfSteppers(): "

        # We will need one stepper for each distinct stepperNum in the 
        # list of steps, so get a list of distinct stepperNums.
        listOfStepperNums = []
        for step in self.stepListContainerObject.listOfSteps:
            if not step.stepperNum in listOfStepperNums:
                listOfStepperNums.append(step.stepperNum)

        listOfStepperNums.sort()

        listOfSteppers = []
        for stepperNum in listOfStepperNums:
            stepper = StepperClass(pfx, self.logObjectContainer, stepperNum, 
                      self.stepListContainerObject)
            listOfSteppers.append(stepper)

        return listOfSteppers


    def runMe(self, pPfx):

        """
        PURPOSE:
            Create a list of the steppers.
            Start running each stepper in a separate thread.
            Generate an HTML file that contains some summary info.
        """

        pfx = pPfx + self.__class__.__name__ + ": runMe()"
        # Create a list of steppers.
        listOfSteppers = self.createListOfSteppers(pfx)

        # Start running each stepper in a separate thread.
        rp = RunParallelClass(pfx, self.logObjectContainer, listOfSteppers)
        rp.runMe(pfx)

        # Generate an HTML file that contains some summary info.
        f = open("./" + self.stepListFileName + ".html", "w")
        s = self.stepListContainerObject.returnMeAsHtml()
        f.write(s)
        f.close()
 
