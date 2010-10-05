# ============================================================================
# COPYRIGHT: Copyright (c) 2010, Mark Gilkey.  All rights reserved.  
# PURPOSE: "Main" / starting point for ParallAssist.
#     To use this, execute:
#         python ParallAssist.py <stepListFileName>
#     for example:
#         python ParallAssist.py sampleStepList2
#     Note that you should specify the step list file name WITHOUT the ".py"
#     extension, even though the file will have that extension.
# AUTHOR: mgilkey
# LAST MODIFIED:
#     2010-10-01 mgilkey
#         I made trivial changes to diagnostic messages and added comments,
#         etc. 
# REVIEWED:
#     2010-10-01 mgilkey
# ============================================================================



# Standard Python libraries
import sys

# Gilkey's "utility" libraries
import errCodes
import LogObject
import LogObjectContainer

# ParallAssist libraries
from StepperListRunner import StepperListRunnerClass
from StepListContainer import StepListContainerClass



# You may set this to a different default step list if you want.  
stepListFileName = "SampleStepList2"


UsageMsg = \
        'USAGE: python ParallAssist.py [<stepListFileName>]'  + \
        '   where <stepListFileName> excludes the ".py" extension.'    + \
        '   If <stepListFileName> is not specified, then '  + \
        '   "sampleStepList2" is used.'



def createLogObject(pPfx, pLogFileName):

    """
    PURPOSE:
        This creates a log object, which allows us to send messages to a log
        file.
    PARAMETERS:
        pfx: This is a string that contains information to help debug 
             problems.  Typically, this is simply a "call stack", i.e. a 
             sequence of names of functions/methods that have called this.
    """

    funcPfx = pPfx + "createLogObject(): "

    displayAlso = True
    appendRule = True

    # Send errors, warnings, and "Info" messages to the log.  
    threshold = errCodes.ES_Info

    log1 = LogObject.LogObjectClass(funcPfx, threshold,
           displayAlso, pLogFileName, appendRule)

    return log1


# ============================================================================

if __name__ == '__main__':

    pfx = "ParallAssist: main(): "

    if len(sys.argv) > 2:
        print("ERROR: Too many command-line parameters.")
        print(UsageMsg)
        print("exiting...")
        sys.exit(-1)

    if len(sys.argv) == 2:
        stepListFileName = sys.argv[1]

    print("DDDIAGNOSTIC: stepListFileName = " + stepListFileName)

    # Create a log object container so that we can log error messages.  
    logObject1 = createLogObject(pfx, stepListFileName + ".log")
    logObjectContainer1 = LogObjectContainer.LogObjectContainerClass(pfx)
    logObjectContainer1.appendLogObject(pfx, logObject1)

    # Diagnostic message.
    msg = "Starting to execute step list: " + stepListFileName + "\n"
    logObjectContainer1.logMsg(pfx, msg, errCodes.ES_Info)

    cmd = "import " + stepListFileName
    exec(cmd)

    expr = stepListFileName + ".stepList"
    stepList1 = eval(expr)
    stepListContainer1 = StepListContainerClass(pfx, logObjectContainer1, 
     stepList1)
    # Optional diagnostic:
    # stepListContainer1.displayMe()

    slrc = StepperListRunnerClass(pfx, logObjectContainer1, 
           stepListContainer1, stepListFileName)
    slrc.runMe(pfx)

