class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        data = [False]* (length-1) + [True]
        for i in range(0, length):
            t = length -1  - i
            for j in range(0, nums[t]+1):
                if data[t+j] == True:
                    data[t] = True
                    break
        return data[0]