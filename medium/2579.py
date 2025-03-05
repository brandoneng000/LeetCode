class Solution:
    def coloredCells(self, n: int) -> int:
        return 1 + n * (n - 1) * 2

    # def coloredCells(self, n: int) -> int:
    #     return 1 + sum(4 * i for i in range(n))

    # def coloredCells(self, n: int) -> int:
    #     res = 1

    #     for i in range(1, n):
    #         res += 4 * i
        
    #     return res
        
def main():
    sol = Solution()
    print(sol.coloredCells(1))
    print(sol.coloredCells(2))

if __name__ == '__main__':
    main()