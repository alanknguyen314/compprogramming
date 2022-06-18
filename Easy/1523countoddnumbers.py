"""
1523. Count Odd Numbers in an Interval Range

Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).
"""
# Runtime: 24 ms, faster than 51.14% of Python online submissions for Count Odd Numbers in an Interval Range.
# Memory Usage: 13.5 MB, less than 10.06% of Python online submissions for Count Odd Numbers in an Interval Range.
class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        
        num = 0
        
        if (low == high) and high%2 != 0:
            return 1
        elif (low == high) and high%2 == 0:
            return 0
        else:
            if low%2 == 0:
                if high%2 == 0:
                    return int((high - low)/2.0)
                elif high%2 != 0:
                    return int((high - low)/2.0) + 1
            elif low%2 != 0:
                    return int((high - low)/2.0) + 1

        return num
            