class Solution:
    def arrangeCoins(self, n: int) -> int:
        def sum_of_nums(end: int) -> int:
            return end * (end + 1) // 2
        
        if n == 1:
            return 1

        num = 1

        while sum_of_nums(num) <= n:
            num += 1

        return num - 1
        
def main():
    sol = Solution()
    print(sol.arrangeCoins(5))
    print(sol.arrangeCoins(8))

if __name__ == '__main__':
    main()