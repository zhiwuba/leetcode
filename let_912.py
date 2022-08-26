class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:

        def swap(data, i, j):
            tmp = data[i]
            data[i] = data[j]
            data[j] = tmp

        def partition(data, start, end):
            pos = random.randint(start, end)
            swap(data, pos, end)

            j = start
            for i in range(start, end):
                if data[i] < data[end]:
                    swap(data, j, i)
                    j += 1
            swap(data, end, j)
            return j

        def quick_sort(data: List[int], start: int, end: int):
            if end - start <= 0:
                return

            idx = partition(data, start, end)
            quick_sort(data, start, idx - 1)
            quick_sort(data, idx + 1, end)

        quick_sort(nums, 0, len(nums) - 1)
        return nums