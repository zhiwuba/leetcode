class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        path = []
        result = []

        def walk(start_index):
            if len(path) == k:
                result.append(path.copy())
                return

            for val in range(start_index, n+1):
                path.append(val)
                walk(val+1)
                path.pop(-1)

        walk(1)

        return result