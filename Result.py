# ============================================================================
# COPYRIGHT: Copyright (c) 2010, Mark Gilkey.  All rights reserved.  
# PURPOSE: Represents a "result" of executing a "statement".
# AUTHOR: mgilkey
# LAST MODIFIED:
# 
# ============================================================================


"""PURPOSE: Represents a "result" of executing a "statement".

This class represents a "result".  This result could be almost anything, so 
one of the things that we indicate is the "type" of the result.

Hmm, should I make this "OOP"ish?  Should there be a parent Result type, 
and each possible result type (integer, string, resultSet, etc.) would have 
its own class with the same methods, such as "equal" (which would return 
True or False depending upon whether the actual and expected results passed 
to the method are equal)?!!!
"""

This should import errCode.py or whatever the latest and greatest version 
of that exists.


class Result:

    # A result is essentially a tuple that contains 2 elements: one 
    # is the result, and one is an indicator of what "type" (integer, 
    # string, array, etc.) the result is.
    # Hmm, if I create a class hierarchy, then I don't need a separate 
    # variable/field/element to indicate the data type of the result; 
    # the result data type is indicated by the class type.


    def getResult(self, pContext):
        return self.result

    def setResult(self, pContext, pResult):
        self.result = pResult

    def equals(self, pContext, pOtherResult):
        """PURPOSE: Compares 2 objects of this type and returns True or False.

        This returns True if the 2 objects are of the same type and returns 
        False if they are not.

        Note that this treats two "None" values as equal.  That may or may 
        not be the behavior that you want.  

        Are there ever circumstances in which you will need to customize 
        this and use this instead of "=="?!!!

        Note that this tests for equality, not set-wise equivalence.  E.g. 
        when getting results back from an SQL statement, the order of the 
        rows may vary, and sets that have the same rows in a different order
        will not look equal.  You may want to write a custom "equals()" 
        method in your subclass if you want equivalent but not equal sets 
        to be considered equal.  
        """

        Check the data type!!!

        if self.result == pOtherResult:
            return True
        else:
            return False
