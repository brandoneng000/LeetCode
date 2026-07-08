from typing import List

MOD = 1_000_000_007
MAX = 100001
pow = [1] * MAX

for i in range(1, MAX):
    pow[i] = (pow[i - 1] * 10) % MOD


class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        res = []
        A, B, Len = [[0] * (n + 1) for _ in range(3)]

        for i in range(n):
            d = int(s[i])
            A[i + 1] = A[i] + d
            B[i + 1] = (B[i] * 10 + d) % MOD if d else B[i]
            Len[i + 1] = Len[i] + (d > 0)
        
        for l, r in queries:
            r += 1
            sub = (B[l] * pow[Len[r] - Len[l]]) % MOD
            x = (B[r] - sub) % MOD
            
            res.append((x * (A[r] - A[l])) % MOD)

        return res
        
        
def main():
    sol = Solution()
    print(sol.sumAndMultiply(s = "10203004", queries = [[0,7],[1,3],[4,6]]))
    print(sol.sumAndMultiply(s = "1000", queries = [[0,3],[1,1]]))
    print(sol.sumAndMultiply(s = "9876543210", queries = [[0,9]]))

if __name__ == '__main__':
    main()