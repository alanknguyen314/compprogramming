"""
217. Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

"""

# Runtime: 517 ms, faster than 49.91% of Python online submissions for Contains Duplicate.
# Memory Usage: 22.5 MB, less than 92.64% of Python online submissions for Contains Duplicate.
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        nums.sort()
        length = len(nums)
        
        for i in range(length - 1):
            if nums[i] == nums[i + 1]:
                return True
        
        return False
            
            
        