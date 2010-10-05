# ---------------------------------------------------------------------------
"""
COPYRIGHT: Copyright (c) 2010, Mark Gilkey.  All rights reserved.
PURPOSE:
        1) Execute statements written in Perl.
DESIRABLE ENHANCEMENTS:
        1) Maintain "context", so that step N can use variables that were 
           set by earlier steps (by the same user).  This "maintain context"
           capability will be new for ParallAssist.  
PRE-REQUISITES:
   This requires that your path include the Perl interpreter, of course.
AUTHOR: mgilkey
ALGORITHM:
    We launch the Perl interpreter by using the Popen() function and 
    specifying input and output streams.  
    I hope that this will allow me to pump in commands and get back output.
    Potential problems include:
        1) Returned values may all be strings, which won't always be what 
           I want.
"""
# ---------------------------------------------------------------------------


import errorCodes

from LanguageSupportCallable import LanguageSupportCallableClass
from LanguageSupport import LanguageSupportClass

class LanguageSupportPerlClass(LanguageSupportCallableClass):

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

      self.language = "Perl"
      self.interpreterProgramName = "perl"
      # The -e indicates that perl should treat the next command line 
      # parameter as a perl statement(s) to be executed, e.g. 
      #    "perl -e '$x = 18; print $x';"
      self.commandLineFlag = "-e"



# ---------------------------------------------------------------------------

def selfTest():

   perlSupportObject = languageSupportPerlClass(None)
   print("DDDIAGNOSTIC: After created perlSupportObject")
   print(perlSupportObject.language)

   stmt = "print 'Hello, world, from perl' "
   perlSupportObject.executeStatement(stmt)


# ---------------------------------------------------------------------------
if __name__ == '__main__':
   selfTest()

