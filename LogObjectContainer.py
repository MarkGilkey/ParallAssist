# ==========================================================================
# COPYRIGHT: Copyright (c) 2008, 2010 Mark Gilkey.  All rights reserved.
# AUTHOR: mgilkey
# ==========================================================================


import LogObject
import errCodes


class LogObjectContainerClass:

   """
   PURPOSE:
      This class stores a list of LogObjectClass objects.
      If you ever want more than one log file (e.g. perhaps one that has 
      detailed diagnostics and one that doesn't), you can create 2 (or more) 
      separate LogObjectClass objects (perhaps with different thresholds)
      and put them in this list.  When you call this ListOfLogObjectClass's
      "logMsg()" method, it will in turn invoke the logMsg() method of
      each of the objects in the list.
   """

   className = "LogObjectContainerClass"


   # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
   def __init__(self, pPfx):

      self.listOfLogObjects = []


   # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
   def appendLogObject(self, pPfx, pLogObject):

      self.listOfLogObjects.append(pLogObject)


   # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
   def logMsg(self, pPfx, pMsg, pSeverity):

      for logObj in self.listOfLogObjects:
         logObj.logMsg(pPfx, pMsg, pSeverity)


# --------------------------------------------------------------------------

def selfTest(pPfx):

    pfx = pPfx + "selfTest(): "

    displayAlso = True
    appendRule = True

    filename = "LogFile1.txt"
    threshold = errCodes.ES_Info
    log1 = LogObject.LogObjectClass(funcPfx, threshold,
           displayAlso, filename, appendRule)

    filename = "LogFile2.txt"
    threshold = errCodes.ES_Warning
    log2 = LogObject.LogObjectClass(funcPfx, threshold,
           displayAlso, filename, appendRule)

    filename = "LogFile3.txt"
    threshold = errCodes.ES_Error
    log3 = LogObject.LogObjectClass(funcPfx, threshold,
           displayAlso, filename, appendRule)

    logContainer = LogObjectContainerClass(funcPfx)
    logContainer.appendLogObject(funcPfx, log1)
    logContainer.appendLogObject(funcPfx, log2)
    logContainer.appendLogObject(funcPfx, log3)

    msg = "Help!  I've been laid off!"
    severity = errCodes.ES_Warning

    logContainer.logMsg(funcPfx, msg, severity)


if __name__ == '__main__':

   funcPfx = "LogObjectContainer: main(): "
   selfTest(funcPfx)
