# ============================================================================
# COPYRIGHT: Copyright (c) 2010, Mark Gilkey.  All rights reserved.  
# PURPOSE: This is a piece of sample code that you can look at and use as a 
#     model for creating a step list.
# AUTHOR: mgilkey
# LAST MODIFIED:
# 
# ============================================================================


from LogObject import LogObjectClass
from LogObjectContainerClass import LogObjectContainerClass
from Step import StepClass
from StepListContainer import StepListContainerClass


class stepList: 


def getStepList():

    pfx = "sampleStepList: "

    logObject1 = LogObjectClass(pfx,
                 0,     # error messages with lower severity are not logged.
                        # Hard-coding a nameless integer value is bad style!!!
                 pDisplayAlso = True, 
                 pFilename = "sampleStepList.log",    # file to write to.
                 pAppend = False)

    listOfLogObjects1 = ListOfLogObjectsClass(pfx)
    listOfLogObjects1.appendLogObject(pfx, logObject1)

    errorContext1 = ErrorContextClass(listOfLogObjects1, pfx)


    stepList1 = StepListContainerClass(errorContext1, [])

    step = StepClass(pContext = errorContext1,
           pStepNum = 1,
           pStepperNum = 1,
           pStatement = "print('Greetings, earthlings.')",
           pLanguage = "Python",
           pTimeLimit = 1,
           pExpectedResult = None, 
           pParallel = False)
    stepList1.append(step)


    step = StepClass(errorContext1,
           pStepNum = 2,
           pStepperNum = 1,
           pStatement = "print('This planet is not civilized.')",
           pLanguage = "Python",
           pTimeLimit = 1,
           pExpectedResult = None, 
           pParallel = False)
    stepList1.append(step)

    return stepList1


# ============================================================================

if __name__ == '__main__':
    
    stepList1 = getStepList()
    stepList1.display()
