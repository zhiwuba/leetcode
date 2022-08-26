class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        path = []

        def walk(cur_target: int, start: int):
            for i in range(start, len(candidates)):
                val = candidates[i]
                path.append(val)
                if cur_target - val == 0:
                    result.append(path.copy())
                elif cur_target - val > 0:
                    walk(cur_target - val, i)
                path.pop(-1)

        walk(target, 0)
        return result