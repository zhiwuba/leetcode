class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1

        max_value = 0
        while i < j:
            value = (j - i) * min(height[i], height[j])
            if value > max_value:
                max_value = value
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_value