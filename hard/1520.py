from typing import List

class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)
        char_start = {}
        char_end = {}
        intervals = []
        res = []

        for i in range(n):
            if s[i] not in char_start:
                char_start[s[i]] = i

            char_end[s[i]] = i

        for c in char_start:
            l, r = char_start[c], char_end[c]
            i = l

            while i <= r:
                if char_start[s[i]] < l:
                    break

                r = max(r, char_end[s[i]])
                i += 1
            else:
                intervals.append((r, l))

        intervals.sort()
        end = -1

        for r, l in intervals:
            if l > end:
                res.append(s[l: r + 1])
                end = r

        return res


def main():
    sol = Solution()
    print(sol.maxNumOfSubstrings("adefaddaccc"))
    print(sol.maxNumOfSubstrings("abbaccd"))

if __name__ == '__main__':
    main()