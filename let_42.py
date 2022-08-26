class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        left_max_heights = [0] * length
        right_max_heights = [0] * length

        left_max_heights[0] = height[0]
        for i in range(1, length):
            left_max_heights[i] = max(left_max_heights[i - 1], height[i])

        right_max_heights[length - 1] = height[length - 1]
        for j in range(length - 2, 0, -1):
            right_max_heights[j] = max(right_max_heights[j + 1], height[j])

        result = 0
        for i in range(1, length - 1):
            water = min(left_max_heights[i], right_max_heights[i]) - height[i]
            if water > 0:
                result += water
        return result