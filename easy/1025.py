class Solution:
    def divisorGame(self, n: int) -> bool:
        return n % 2 == 0

def main():
    sol = Solution()
    print(sol.divisorGame(2))
    print(sol.divisorGame(3))

if __name__ == '__main__':
    main()