class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:

        def split(version):
            parts = version.split(".")
            return [int(item) for item in parts]

        num1 = split(version1)
        num2 = split(version2)

        i = 0
        while (i < len(num1) and i < len(num2)):
            if num1[i] > num2[i]:
                return 1
            elif num1[i] < num2[i]:
                return -1
            i += 1

        while (i < len(num1)):
            if num1[i] > 0:
                return 1
            i += 1
        while (i < len(num2)):
            if num2[i] > 0:
                return -1
            i += 1
        return 0
