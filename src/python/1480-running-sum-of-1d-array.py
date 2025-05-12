class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        
        running_sum = []
        counter = 0

        for num in nums:
            counter += num
            running_sum.append(counter)
        
        return running_sum