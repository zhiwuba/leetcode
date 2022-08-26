class Solution:
    def numTrees(self, n: int) -> int:
        data = [0] * (n+1)
        data[0] = 1
        data[1] = 1

        for i in range(2, n+1):
            for j in range(1, i+1):
                data[i] += data[j-1] * data[i-j]
        return data[n]