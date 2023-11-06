class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        res = 0

        for i in range(n):
            for j in range(m):
                miss, pos = 0, 0

                while i + pos < n and j + pos < m and miss < 2:
                    miss += s[i + pos] != t[j + pos]
                    res += miss == 1
                    pos += 1
        
        return res

        
def main():
    sol = Solution()
    print(sol.countSubstrings(s = "aba", t = "baba"))
    print(sol.countSubstrings(s = "ab", t = "bb"))

if __name__ == '__main__':
    main()