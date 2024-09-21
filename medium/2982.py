from collections import defaultdict

class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        freq = defaultdict(lambda: [0] * (n + 1))
        prev = s[0]

        size = 1
        freq[s[0]][1] = 1
        res = -1

        for i in range(1, n):
            cur = s[i]

            if cur == prev:
                size += 1
                freq[cur][size] += 1
            else:
                freq[cur][1] += 1
                prev = cur
                size = 1
        
        for key in freq:
            pre_sum = 0

            for j in range(n, 0, -1):
                pre_sum += freq[key][j]

                if pre_sum >= 3:
                    res = max(res, j)
                    break

        return res
        
def main():
    sol = Solution()
    print(sol.maximumLength("aaaa"))
    print(sol.maximumLength("abcdef"))
    print(sol.maximumLength("abcaba"))

if __name__ == '__main__':
    main()