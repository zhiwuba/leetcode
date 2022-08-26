class Solution:
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        total = len(nums)
        for i in range(0, total):
            for j in range(i+1, total):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}
        for i in range(0, len(nums)):
            diff = target - nums[i]
            if diff in mapping:
                return [i, mapping[diff]]
            else:
                mapping[nums[i]] = i
        return []