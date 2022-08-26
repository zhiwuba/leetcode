class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        data = [0] * length
        data[length-1] = prices[length-1]
        for i in range(length-2, -1, -1):
            data[i] = max(prices[i], data[i+1])
        result = 0
        for i in range(0, length):
            diff = data[i] - prices[i]
            if diff > result:
                result = diff
        return result

    def maxProfit2(self, prices: List[int]) -> int:
        result = 0
        for i in range(0, len(prices)):
            for j in range(i+1, len(prices)):
                diff = prices[j] - prices[i]
                if diff > result:
                    result = diff
        return result