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
      I corrected an inconsistency between the code and comments in the 
         executeStatementAndReturnValue() method.  
LAST CODE REVIEWED:
   2010-07-30 mgilkey
"""
# ---------------------------------------------------------------------------


import errorCodes

from LanguageSupport import LanguageSupportClass


class LanguageSupportPythonExecClass(LanguageSupportClass):

   """
   PURPOSE
      This base class provides a standard way to execute statements
      written in the Python language.  Note that this is still somewhat
      limited because the return type of every statement that you
      might execute is not necessarily the same.  (The return type
      could be None, integer, class, list, ...)
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

      self.language = "PythonExec"

      # For Python, there isn't much else that we need to do.
      # We don't even need the pContext parameter.



   def executeStatementAndReturnValue(self, stmt, pLocals = None):

      """
      PURPOSE:
         This executes a Python statement.  
         If you'd like to get a value (other than an error indicator) 
         returned, then you probably should use the 
         LanguageSupportPythonEval class.  
      RETURNS:
         If an error is detected, this currently returns -1.  
         Otherwise, it returns None.
      DESIRABLE ENHANCEMENT:
         1) If the eval() function can throw an exception, then I probably
            ought to catch it and return some type of error indicator!!!
      """

      rc = None
      if stmt == None or stmt == "":
         rc = -1   # Use a more helpful error code!!!
         # !!! Throw an exception!?
      else:
         # I probably should be catching exceptions here and returning 
         # something other than None!!!
         exec(stmt, globals(), pLocals)
      return rc


# ---------------------------------------------------------------------------

def selfTest():

   pythonSupportObject = LanguageSupportPythonExecClass(None)

   stmt = "print('foo')"
   pythonSupportObject.executeStatementAndReturnValue(stmt)


# ---------------------------------------------------------------------------
if __name__ == '__main__':
   selfTest()

