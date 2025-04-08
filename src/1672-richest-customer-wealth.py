class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max_num = 0

        for i in range(len(accounts)):
            max_num = max(max_num, sum(accounts[i]))
        
        return max_num