class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(i, j):
            tmp = nums[i]
            nums[i]= nums[j]
            nums[j] = tmp

        p0 = 0
        p2 = len(nums) - 1
        i = 0

        while i <= p2:
            while i <= p2 and nums[i] == 2:
                swap(i, p2)
                p2 -= 1

            if nums[i] == 0:
                swap(i, p0)
                p0 += 1
            i += 1