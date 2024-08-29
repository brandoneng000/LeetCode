class Solution:
    def sumOfMultiples(self, n: int) -> int:
        res = 0

        for num in range(3, n + 1, 3):
            res += num

        for num in range(5, n + 1, 5):
            if num % 3 == 0:
                continue

            res += num
        
        for num in range(7, n + 1, 7):
            if num % 3 == 0 or num % 5 == 0:
                continue

            res += num
        
        return res
        
def main():
    sol = Solution()
    print(sol.sumOfMultiples(7))
    print(sol.sumOfMultiples(10))
    print(sol.sumOfMultiples(9))

if __name__ == '__main__':
    main()