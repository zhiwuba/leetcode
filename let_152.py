class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        min_values = [0] * len(nums)
        max_values = [0] * len(nums)

        min_values[0] = nums[0]
        max_values[0] = nums[0]

        score = nums[0]

        for i in range(1, len(nums)):
            min_values[i] = min(nums[i], min(min_values[i-1]*nums[i], max_values[i-1]*nums[i] ))
            max_values[i] = max(nums[i], max(max_values[i-1]*nums[i], min_values[i-1]*nums[i] ))

            if max_values[i] > score:
                score = max_values[i]
        return score