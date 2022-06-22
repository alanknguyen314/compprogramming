"""
1672. Richest Customer Wealth

You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

"""
# 83 ms
# 13.4 MB
# 06/18/2022 20:21

class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        def sumlist(list1):
            sumtot = 0
            for i in list1:
                sumtot += i
            return sumtot
        
        maxlocal = 0
        empval = 0
        emplist = []
        
        for i in range(len(accounts)):
            empval = sumlist(accounts[i])
            emplist.append(empval)    
            maxlocal = max(maxlocal, empval)
        return maxlocal
            
                
                
            
                
                