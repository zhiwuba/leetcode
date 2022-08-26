from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def match(part: str):
            print(part)

            for word in wordDict:
                if part.startswith(word):
                    part2 = part[len(word):]
                    if not part2:
                        return True

                    ret = match(part2)
                    if ret:
                        return True
            return False

        return match(s)


if __name__ == '__main__':
    s = Solution()
    print(s.wordBreak("cars", ["car", "ca", "rs"]))
