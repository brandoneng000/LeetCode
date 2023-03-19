class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return num == 0 or num % 10 != 0

def main():
    sol = Solution()
    print(sol.isSameAfterReversals(526))
    print(sol.isSameAfterReversals(1800))
    print(sol.isSameAfterReversals(0))

if __name__ == '__main__':
    main()