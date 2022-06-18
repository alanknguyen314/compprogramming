"""
1480. Running Sum of 1d Array

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.
"""

# Runtime: 153 ms, faster than 5.08% of Python online submissions for Running Sum of 1d Array.
# Memory Usage: 13.6 MB, less than 60.54% of Python online submissions for Running Sum of 1d Array.
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        emplist = []
        newlist = nums[:]
        for i in range(len(newlist)):
            n = 0
            while n < i:
                newlist[i] += nums[n] 
                n += 1
        return newlist


# RUNTIME: 18ms
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer=[]
        tmp=0
        for i in nums:
            tmp+=i
            answer.append(tmp)
        return answer