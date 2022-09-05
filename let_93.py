from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        length = len(s)

        def is_valid(part):
            if len(part) == 0:
                return False

            if part.startswith("0"):
                if len(part) == 1:
                    return True
                else:
                    return False
            else:
                if 0 < int(part) <= 255:
                    return True
                else:
                    return False

        result = []
        for i in range(1, max(3, length)):
            item = []
            if not is_valid(s[0:i]):
                break
            item.append(s[0:i])

            for j in range(i + 1, max(i + 3, length)):
                if not is_valid(s[i:j]):
                    break
                item.append(s[i:j])

                for m in range(j + 1, max(j + 3, length)):
                    if not is_valid(s[j:m]):
                        break
                    if is_valid(s[m:]):
                        item.append(s[j:m])
                        item.append(s[m:])
                        result.append(".".join(item))
                        item.pop(-1)
                        item.pop(-1)
                item.pop(-1)
        return result