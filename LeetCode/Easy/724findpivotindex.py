"""
724. Find Pivot Index

Given an array of integers nums, calculate the pivot index of this array.
The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.
Return the leftmost pivot index. If no such index exists, return -1.
"""

# Runtime: 119 ms, faster than 91.59% of Python online submissions for Find Pivot Index.
# Memory Usage: 14.6 MB, less than 44.14% of Python online submissions for Find Pivot Index.
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        def sum(list1):
            ans = 0
            for i in list1:
                ans += i
            return ans
        
        totalsum = sum(nums)
        tmp = 0
        n = 0
        
        for i in nums:
            tmp += i
            if (tmp - i) == (totalsum - i)/2.0:
                return n
            n += 1
            
        return -1