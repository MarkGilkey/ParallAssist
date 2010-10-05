# ---------------------------------------------------------------------------
"""
COPYRIGHT: Copyright (c) 2009 - 2010, Mark Gilkey.  All rights reserved.
PURPOSE: This base class is an API that provides a standard way to execute
   statements written in different languages.
WARNINGS:
   1) This is very limited right now, in large part because it 
      doesn't provide good support for handling the value (if any)
      returned by the execution of the statement.
PRE-REQUISITES:
   This requires Python 2.6 or later (although I suspect that with
   minor modifications it would work with versions of Python at least
   as far back as 2.3, which is the earliest version that I've used and
   know anything about).  
AUTHOR: mgilkey
LAST MODIFIED:
LAST TIME REVIEWED:
   2010-07-30 mgilkey
"""
# ---------------------------------------------------------------------------


import errorCodes


class LanguageSupportClass:

   """
   PURPOSE
      This base class provides a standard way to execute statements
      written in different languages.  It does this by providing a
      standard set of methods that a caller may use.  For example, there
      is an "execute a statement" method that takes a statement in the
      language and executes it, then returns to the caller some type
      of result (which might be an error code, a value, or a class
      object, or something else such as a list of lists.
   """

   def __init__(self, pContext):

      """
      PARAMETERS:
         pContext is some type of "thing" that provides enough information
            for the class to initialize itself.  The exact structure of the
            "thing" depends upon what the derived class needs.  For example,
            if the language is Perl, you might supply information that
            would help you invoke a Perl interpreter.  If 
            the language is SQL, you might pass some type of database
            connection or you might pass the information needed to
            establish such a connection.
      """

      self.language = "Specify a language here!"
      self.context = pContext
      print("Customize this for your chosen language!!!")


   def getLanguage(self):
      """
      PURPOSE:
         Return the name of the language, e.g. "Python", "SQL", etc.
      """
      return self.language


   def executeStatement(self, stmt):
      print("Customize this executeStatement() method for your language!!!")
      return 0   # Some error/success indicator.  Or should I use exceptions?!!!


   def executeStatementAndReturnValue(self, cmd, pThisStep = None, 
    returnStdout = True, returnStderr = True):
        """PURPOSE: execute a statement and return results.

        This executes a statement(s) written in the language (e.g. Python) 
        that is supported by this LanguageSupport class.

        If the statement executes without (detected) error, then we 
        return the result in the form of a "Result" object.

        If there was an error, we throw an exception (or at least in 
        the future we should -- I don't think I do it yet!!!).  So far, I don't 
        have more detailed info about the exception thrown.  
        """ 

        print("Customize this for your chosen language!!!")
        return 0   # Should return the value that results from executing the stmt!!!
