# ---------------------------------------------------------------------------
"""
COPYRIGHT: Copyright (c) 2009, 2010 Mark Gilkey.  All rights reserved.
PRE-REQUISITES:
   This requires Python 2.6 or later (although I suspect that with
   minor modifications it would work with versions of Python at least
   as far back as 2.3, which is the earliest version that I've used and
   know anything about).  
AUTHOR: mgilkey
LAST MODIFIED:
   2010-07-30 mgilkey
      I removed some unused code.
      I updated some comments to reflect that this is the "...Eval" rather 
         than the "...Exec" class.
      I updated the selfTest() function.
LAST CODE REVIEWED:
   2010-07-30 by mgilkey
"""
# ---------------------------------------------------------------------------


# Import some semi-standard error codes.
import errorCodes

from LanguageSupport import LanguageSupportClass


class LanguageSupportPythonEvalClass(LanguageSupportClass):

   """
   PURPOSE
      This base class provides a standard way to evaluate expressions 
      written in the Python language.  
   """

   def __init__(self, pContext = None):

      """
      PARAMETERS:
         pLanguage:
            The name of the language that this object "supports", for
            example: "Python", "SQL", etc.
         pContext is some type of "thing" that provides enough information
            for the class to initialize itself.  The exact structure of the
            "thing" depends upon what the derived class needs.  For example,
            if the language is SQL, you might pass some type of database
            connection or you might pass the information needed to
            establish such a connection.
      """

      self.language = "PythonEval"

      # For Python, there isn't much else that we need to do.
      # We don't even need the pContext parameter.


   def executeStatementAndReturnValue(self, stmt, pLocals):

      """
      PURPOSE:
         This evaluates a python expression and returns the value.  Note 
         that if you want to execute a Python statement, as opposed to 
         evaluate an expression, you should use the 
         LanguageSupportPythonExec class.  
      RETURNS:
         The value that the expression evaluates to.  
      DESIRABLE ENHANCEMENT:
         1) If the eval() function can throw an exception, then I probably
            ought to catch it and return some type of error indicator.
      """

      if stmt == None or stmt == "":
         rc = -1   # Use a more helpful error code!!!
         # !!! Throw an exception!?
      else:
         rc = eval(stmt, globals(), pLocals)
      return rc


# ---------------------------------------------------------------------------

def selfTest():

   pythonSupportObject = LanguageSupportPythonEvalClass(None)

   stmt = "(2 * 3 * 4)"
   rc = pythonSupportObject.executeStatementAndReturnValue(stmt)
   print(rc)   # Should be 24
   if (rc == 24):
      print("Passed sanity self test.")
   else:
      print("Failed sanity self test.")



# ---------------------------------------------------------------------------
if __name__ == '__main__':
   selfTest()

