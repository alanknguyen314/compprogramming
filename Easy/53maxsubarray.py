"""
53. Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
A subarray is a contiguous part of an array.
I learned Kadane's Algorithm from this question.
Reference: https://en.wikipedia.org/wiki/Maximum_subarray_problem

"""
# Runtime: 824 ms, faster than 44.17% of Python online submissions for Maximum Subarray.
# Memory Usage: 25.7 MB, less than 46.53% of Python online submissions for Maximum Subarray.
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Implementation of Kadane's Algorithm.
        
        def allneg(list1):
            for i in list1:
                if i > 0:
                    return False
            return True
        
        if len(nums) == 1:
            return nums[0]
        elif allneg(nums) == True:
            return max(nums)
        else:
            best_sum = 0
            current_sum = 0
            for x in nums:
                current_sum = max(0, current_sum + x)
                best_sum = max(best_sum, current_sum)
            
            return best_sum
        