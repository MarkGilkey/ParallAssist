# ============================================================================
# COPYRIGHT: Copyright (c) 2010, Mark Gilkey.  All rights reserved.  
# PURPOSE:  This class represents a "stepper" that can run 0 or more steps in 
#    a list of steps.
# AUTHOR: mgilkey
# WARNINGS: 
#     This code has one probable minor bug and one piece of code that won't 
#     work if we run steps in parallel in the future.  Search for "!!!".  
# LAST MODIFIED:
#     2010-10-01 mgilkey
#         I added some comments.  
#         I fixed a probable bug by adding the startTimeOfCurrentStep()
#             method and calling that rather than time.time().
# REVIEWED:
#     2010-10-01 mgilkey
# ============================================================================



import time

import errCodes

import Runnable


class StepperClass(Runnable.RunnableClass):

    # The number of seconds to wait in between checks to see whether the 
    # previous step has completed.  
    SleepLength = 1.0

    def __init__(self, pPfx, pLogObjectContainer, pStepperNum, 
     pStepListContainer):
        """PURPOSE: Initialize a stepper with info about its stepper num, etc.
        PARAMETERS: 
            pPfx: the usual "call stack" in the form of a string (for debug).
            pLogObjectContainer: the usual variable with info about error logs, etc.
            pStepperNum: This indicates which stepper this is (so that this 
               stepper knows which steps in the list to run).
            pStepListContainer: The list of steps to execute, along with 
               associated info, such as the step number of the next step 
               to execute.  If I remember correctly, this 
               is the list of ALL steps, not just the steps for this stepper.
               This stepper must run only his own steps, of course.
        """

        pfx = pPfx + self.__class__.__name__ + ": __init__(): "

        self.logObjectContainer = pLogObjectContainer
        self.stepperNum = pStepperNum
        self.stepListContainer = pStepListContainer

        if pStepListContainer == None or len(pStepListContainer.listOfSteps) < 1:
            msg = "ERROR: " + pfx
            msg += "No steps in pStepList."
            print(msg)
            self.listOfLogObjects.logMsg(pfx, msg, errCodes.ES_FatalError)
            # ... and throw an exception!!!

        # Set myNextStepNum, which indicates the step number of the next 
        # (in this case first) step that this stepper should run.  
        self.myNextStepNum = self.getMyNextStepNum(pfx, pStart = 0)
        if self.myNextStepNum == None or self.myNextStepNum < 0 or \
         self.myNextStepNum > self.stepListContainer.numSteps + 1:
            msg = "ERROR: " + pfx
            msg += "No steps in pStepList for stepper number " 
            msg += str(self.stepperNum)
            print(msg)
            self.logObjectContainer.logMsg(pfx, msg, errCodes.ES_FatalError)
            # ... and throw an exception!!!


    def getMyNextStepNum(self, pPfx, pStart = None):

        """PURPOSE: Get myNextStepNum, which is the step number of the next 
        step that this stepper should run.  Returns None if there are no more 
        steps for this stepper to run.
        PARAMETERS:
            pStart indicates which step to start searching from.  If we're 
                searching for the first step that this stepper should execute,
                then pStart should be 0.  Otherwise, we typically start from 
                one past the last step completed, or at least the last step 
                that this particular stepper completed.  
        """

        if pStart == None and self.myNextStepNum == None:
            return None

        if pStart != None:
            stepNum = pStart
        else:
            stepNum = self.myNextStepNum + 1
        numSteps = len(self.stepListContainer.listOfSteps)

        # While we haven't reached the end of the list of steps and 
        # we haven't found a step with a matching stepperNum...
        while stepNum < numSteps and \
         self.stepListContainer.listOfSteps[stepNum].stepperNum != self.stepperNum:
            stepNum += 1

        if stepNum >= numSteps:
            return None
        if self.stepListContainer.listOfSteps[stepNum].stepperNum != self.stepperNum:
            return None
        return stepNum


    def timeToWaitBeforeExecutingStep(self):
        """PURPOSE: Calculate max time to wait before executing this step.
        PARAMETERS:
            pStepList: The list of all the steps to be executed.  We need 
                this so that we can read the timeout values of steps.  
            pMyNextStepNum: The step number for which we are trying to 
                calculate the maximum wait time.
        ALGORITHM: Given "N", which is the step number of the step for 
            which we want to calculate the maximum wait time, and step 
            "L", which is the last step completed, the wait for step N 
            should be no more than the sum of the maximum allowable 
            durations for steps L+1 to N-1.  
            E.g. if we've finished step 2, and we want to know the maximum 
            time to wait before running step 5, the max is the sum of the 
            maximum allowable durations for steps 3 and 4.
            Note that it's important to re-calculate this after each step 
            has completed, because steps usually run in less time than the 
            maximum that they are allowed.  
        RETURNS: maximum time (in seconds) to wait before running step 
            number pMyNextStepNum.
        """

        maxWait = 0
        currentStepNum = self.stepListContainer.lastStepNumCompleted + 1
        myNextStepNum = self.myNextStepNum
        for i in range(currentStepNum, myNextStepNum):
            step = self.stepListContainer.listOfSteps[i]
            maxWait += step.timeLimit
        return maxWait


    def startTimeOfCurrentStep(self):
        lastStepNumCompleted = self.stepListContainer.lastStepNumCompleted
        if lastStepNumCompleted == None:
            currentStepNum = 0
        else: 
            currentStepNum = lastStepNumCompleted + 1
        currentStep = self.stepListContainer.listOfSteps[currentStepNum]
        return currentStep.startTime


    def waitUntil(self):
        """PURPOSE: Calculate time at which specified step should run.

           This calculates the time at which the specified step should run, 
           assuming that all not-yet-run steps prior to the specified step 
           time out rather than finish executing.
           In reality, most steps complete rather than time out, but this 
           function gets called pretty frequently to re-calculate the 
           time that we should wait until.  
        PARAMETERS:
            pStepList: The list of all the steps to be executed.  We need 
                this so that we can read the timeout values of steps.  
            pStepNum: The step number for which we are trying to calculate 
                the maximum wait time.
        ALGORITHM: Given "N", which is the step number of the step for 
            which we want to calculate the maximum wait time, and step 
            "L", which is the last step completed, the wait for step N 
            should be no more than the sum of the maximum allowable 
            durations for steps L+1 to N-1.  
            E.g. if we've finished step 2, and we want to know the maximum 
            time to wait before running step 5, the max is the sum of the 
            maximum allowable durations for steps 3 and 4.
            Note that it's important to re-calculate this after each step 
            has completed!
        RETURNS: maximum time (in seconds) to wait before running step 
            number pMyNextStepNum.

        """

        waitTime = self.timeToWaitBeforeExecutingStep()
        waitUntilTime = startTimeOfCurrentStep() + waitTime
        # print("DDDIAGNOSTIC: waitUntilTime = ", waitUntilTime)
        return waitUntilTime


    def previousStepsHaveNotTimedOut(self):
        if time.time() < self.waitUntil():
            return True
        return False


    def runMe(self, pPfx):

        pfx = pPfx + self.__class__.__name__ + ": runMe(): "

        if self.myNextStepNum == None:
            myNextStep = None
        else:
            myNextStep = self.stepListContainer.listOfSteps[self.myNextStepNum]

        # While I haven't finished all the steps in the list that I'm 
        # supposed to run...
        while myNextStep != None:

            # While we haven't reached the end of the list of steps AND 
            # we haven't reached the last step for this stepper to run AND 
            # the most recently completed step is less than 
            #     the step before this one AND 
            # we haven't timed out the previous step(s) AND
            # this step is not supposed to be run in parallel with the prevous
            # one...
            while self.stepListContainer.lastStepNumCompleted < len(self.stepListContainer.listOfSteps) and \
             self.myNextStepNum != None and \
             self.stepListContainer.lastStepNumCompleted < (self.myNextStepNum - 1) and \
             self.previousStepsHaveNotTimedOut() and \
             myNextStep.parallel != True:
                # print("DDDIAGNOSTIC: sleeping")
                # print(self.stepListContainer.lastStepNumCompleted)
                time.sleep(StepperClass.SleepLength)

            # --- Run the step. ---
            myNextStep.runMe(pfx)

            # Mark the step completed.  
            # The following is not thread safe if steps are run in parallel!!!
            self.stepListContainer.lastStepNumCompleted = myNextStep.stepNum

            # Figure out which step I'm supposed to run next.
            self.myNextStepNum = self.getMyNextStepNum(pfx)
            if self.myNextStepNum == None:
                myNextStep = None
            else:
                myNextStep = self.stepListContainer.listOfSteps[self.myNextStepNum]

# ----------------------------------------------------------------------------


def selfTest():
    stepper1 = stepper()


if __name__ == '__main__':
    selfTest()