class Solution:
    def minOperations(self, n: int) -> int:
        res = 0
        goal = 2 * (n // 2) + (n & 1)

        for i in range(n // 2):
            res += goal - (2 * i + 1)

        return res
    
def main():
    sol = Solution()
    print(sol.minOperations(3))
    print(sol.minOperations(6))

if __name__ == '__main__':
    main()