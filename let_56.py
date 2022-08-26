class Solution:

    def can_merge(self, a: List[int], b: List[int]) -> List[int]:
        if a[1] < b[0] or a[0] > b[1]:
            return False
        return True

    def merge_list(self, a: List[int], b: List[int]) -> List[int]:
        return [min(a[0], b[0]),  max(a[1], b[1])]

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort(key=lambda item: item[0])
        for i in range(0, len(intervals)):
            if not result:
                result.append(intervals[0])
            else:
                if self.can_merge(result[-1], intervals[i]):
                    result[-1] = self.merge_list(result[-1], intervals[i])
                else:
                    result.append(intervals[i])
        return result