class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        windows = []
        for i in range(0, len(s)):
            for j in range(i, len(s)):
                if s[j] in windows:
                    if len(windows) > max_length:
                        max_length = len(windows)
                    windows = []
                    break
                else:
                    windows.append(s[j])
        if len(windows) > max_length:
            max_length = len(windows)
        return max_length
