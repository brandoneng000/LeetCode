class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 1_000_000_007
        n = len(s)
        dp = [1]
        last = {}

        for i in range(n):
            dp.append(dp[-1] * 2)

            if s[i] in last:
                dp[-1] -= dp[last[s[i]]]

            last[s[i]] = i

        return (dp[-1] - 1) % MOD

def main():
    sol = Solution()
    print(sol.distinctSubseqII("abc"))
    print(sol.distinctSubseqII("aba"))
    print(sol.distinctSubseqII("aaa"))

if __name__ == '__main__':
    main()