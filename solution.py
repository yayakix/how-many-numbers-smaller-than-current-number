class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # loop
        # when on number
        # if number in loop greater or less than
        ans = []
        for x in range(len(nums)):
            currNum = nums[x]
            currCount = 0
            for x in range(len(nums)):
                if nums[x] < currNum:
                    currCount = currCount + 1
            ans.append(currCount)
        return ans
