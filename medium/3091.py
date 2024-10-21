class Solution:
    def minOperations(self, k: int) -> int:
        if k == 1:
            return 0

        res = float('inf')

        for i in range(k):
            cur = 1 + i
            res = min(res, k // cur + i - (1 if k % cur == 0 else 0))
        
        return res

        
def main():
    sol = Solution()
    print(sol.minOperations(6))
    print(sol.minOperations(11))
    print(sol.minOperations(1))

if __name__ == '__main__':
    main()