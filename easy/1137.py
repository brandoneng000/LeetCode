class Solution:
    def tribonacci(self, n: int) -> int:
        if not n:
            return 0
        elif n == 1 or n == 2:
            return 1
        first = 0
        second = 1
        third = 1

        for _ in range(n - 2):
            first, second, third = second, third, first + second + third
        
        return third

def main():
    sol = Solution()
    print(sol.tribonacci(4))
    print(sol.tribonacci(25))

if __name__ == '__main__':
    main()