"""
1491. Average Salary Excluding the Minimum and Maximum Salary

You are given an array of unique integers salary where salary[i] is the salary of the ith employee.
Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5 of the actual answer will be accepted.
"""

# Runtime: 24 ms, faster than 59.86% of Python online submissions for Average Salary Excluding the Minimum and Maximum Salary.
# Memory Usage: 13.4 MB, less than 72.13% of Python online submissions for Average Salary Excluding the Minimum and Maximum Salary.
class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        
        def sumlist(list1):
            sumtotal = 0
            for i in list1:
                sumtotal += i
            return sumtotal
        
        return((sumlist(salary) - max(salary) - min(salary))/float((len(salary) - 2)))