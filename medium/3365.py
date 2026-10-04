from collections import Counter

class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        n = len(s)
        size = n // k
        cur = Counter()
        goal = Counter()

        for i in range(0, n, size):
            cur[s[i: i + size]] += 1
            goal[t[i: i + size]] += 1

        return cur == goal


def main():
    sol = Solution()
    print(sol.isPossibleToRearrange(s = "abcd", t = "cdab", k = 2))
    print(sol.isPossibleToRearrange(s = "aabbcc", t = "bbaacc", k = 3))
    print(sol.isPossibleToRearrange(s = "aabbcc", t = "bbaacc", k = 2))

if __name__ == '__main__':
    main()