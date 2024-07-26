class Solution:
    def minimumCost(self, s: str) -> int:
        n = len(s)
        res = 0

        for i in range(1, n):
            if s[i] != s[i - 1]:
                res += min(i, n - i)
        
        return res
        
def main():
    sol = Solution()
    print(sol.minimumCost("0011"))
    print(sol.minimumCost("010101"))

if __name__ == '__main__':
    main()