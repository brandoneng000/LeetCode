class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = num2 = 0

        for i in range(1, n + 1):
            if i % m:
                num1 += i
            else:
                num2 += i
        
        return num1 - num2
        
    # def differenceOfSums(self, n: int, m: int) -> int:
    #     return sum(i for i in range(1, n + 1) if i % m) - sum(i for i in range(1, n + 1) if i % m == 0)
        
def main():
    sol = Solution()
    print(sol.differenceOfSums(n = 10, m = 3))
    print(sol.differenceOfSums(n = 5, m = 6))
    print(sol.differenceOfSums(n = 5, m = 1))

if __name__ == '__main__':
    main()