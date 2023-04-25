class Solution:
    def numberOfCuts(self, n: int) -> int:
        if n == 1:
            return 0
        elif n % 2:
            return n
        else:
            return n // 2

def main():
    sol = Solution()
    print(sol.numberOfCuts(4))
    print(sol.numberOfCuts(3))

if __name__ == '__main__':
    main()