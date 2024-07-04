class Solution:
    def coloredCells(self, n: int) -> int:
        res = 1

        for i in range(1, n):
            res += 4 * i
        
        return res
        
def main():
    sol = Solution()
    print(sol.coloredCells(1))
    print(sol.coloredCells(2))

if __name__ == '__main__':
    main()