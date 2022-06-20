"""
2011. Final Value of Variable After Performing Operations

There is a programming language with only four operations and one variable X:

    ++X and X++ increments the value of the variable X by 1.
    --X and X-- decrements the value of the variable X by 1.

Initially, the value of X is 0.

Given an array of strings operations containing a list of operations, return the final value of X after performing all the operations.

"""
# 65 ms
# 13.4 MB
# 06/18/2022 20:24

class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        ans = 0
        
        for i in range(len(operations)):
            if operations[i] == "--X" or operations[i] == "X--":
                ans -= 1
            elif operations[i] == "++X" or operations[i] == "X++":
                ans += 1
                
        return ans
                
