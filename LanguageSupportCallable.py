# ---------------------------------------------------------------------------
"""
COPYRIGHT: Copyright (c) 2009 - 2010, Mark Gilkey.  All rights reserved.
PURPOSE: This class makes it easier to create a new language support object 
   that works by calling an interpreter and passing the executable statement 
   as a string on the command line for the interpreter to execute.  
   For example, to run a statement in perl, you want to invoke the perl 
   interpreter and pass it a statement on the command line.  
       perl -e "MyExecutablePerlStatement"
   For any language that has an interpreter and allows statement(s) to be 
   passed on the command line, you can simply create a subclass of this 
   class, specify the name of the executable file that contains the 
   interpreter (e.g. "perl"), the command line flag that says to read the 
   statement from the command line (e.g. "-e" in the case of perl), and 
   the statement to execute.
   By subclassing this class, you can easily invoke any interpreter and pass 
   it a statement.
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
   2010-09-17 mgilkey
LAST TIME REVIEWED:
"""
# ---------------------------------------------------------------------------

import subprocess

import errorCodes


class LanguageSupportCallableClass:

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
         pContext must provide the following information:
             pContext.languageName:
                 The name of the language; this must match the name of the 
                 language specified in the steps.
             pContext.interpreterProgramName:
                 This is the name of the file/program 
                 that is the interpreter, e.g. "perl" for Perl.  Your PATH must 
                 be sert to enable you to find that file, of course.
             pContext.interpreterProgramName:
                The commandLineFlag is a string that contains the flag that
                tells the interpreter to treat the next item on the command 
                line as a statement to execute.  For example, if you're 
                invoking the Perl interpreter then you will use a command like:
                    perl -e "print 'Hello World'"
                in which case "-e" is the commandLineFlag.  
      """

      self.context = pContext
      self.language = pContext.languageName
      self.interpreterProgramName = pContext.interpreterProgramName
      self.commandLineFlag = pContext.commandLineFlag


   def executeStatement(self, stmt):
      argArray = [self.interpreterProgramName, self.commandLineFlag, stmt]
      print("DDDIAGNOSTIC: LanguageSupportCallableObject: executeStatement()")
      print(argArray)
      p = subprocess.Popen(argArray, stdout=subprocess.PIPE,
          stderr=subprocess.PIPE, universal_newlines=True)
      sout = p.stdout.readlines()
      serr = p.stderr.readlines()
      print("DDDIAGNOSTIC: LanguageSupportCallableObject: executeStatement():")
      print("- - - stdout - - -")
      print(sout)
      print("- - - stderr - - -")
      print(serr)
      return 0   # Someday, return non-zero if we detect error.  
 

   def executeStatementAndReturnValue(self, stmt, pThisStep = None, returnStdout = True, 
    returnStderr = True):
        """PURPOSE: execute a statement and return results.

        This executes a statement(s) written in the language (e.g. Perl) 
        that is supported by this LanguageSupport class.

        If the statement executes without (detected) error, then we 
        return the result.

        If there was an error, we throw an exception.  So far, I don't 
        have more detailed info about the exception thrown.  
        DESIRABLE ENHANCEMENTS:
             This method should throw an exception if there is an error.
        """ 

        argArray = [self.interpreterProgramName, self.commandLineFlag, stmt]
        p = subprocess.Popen(argArray, stdout=subprocess.PIPE,
            stderr=subprocess.PIPE, universal_newlines=True)
        sout = p.stdout.readlines()
        serr = p.stderr.readlines()
        p.wait()

        # Optional diagnostics
        print("DDDIAGNOSTIC: LanguageSupportCallableObject: executeStatementAndReturnValue():")
        print("- - - stdout - - -")
        print(sout)
        print("- - - stderr - - -")
        print(serr)

        # Assemble the value to return.
        retVal = []
        if returnStdout == True and sout != None:
            # Add a check to verify that the Type is list, and handle both 
            # cases (list and non-list)!!!
                for r in sout:
                    retVal.append(r)
        if returnStderr == True and serr != None:
            # Add a check to verify that the Type is list, and handle both 
            # cases (list and non-list)!!!
                for r in serr:
                    retVal.append(r)

        return retVal;
