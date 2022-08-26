class Solution:
    def rob(self, nums: List[int]) -> int:
        data = [0]* len(nums)
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        data[0] = nums[0]
        data[1] = nums[1]

        for i in range(2, len(nums)):
            if i ==2:
                data[i] = data[i-2] + nums[i]
            else:
                data[i] = max(data[i-2], data[i-3]) + nums[i]
        money = 0
        for i in data:
            if i >=money:
                money = i
        return money