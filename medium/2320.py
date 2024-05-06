class Solution:
    def countHousePlacements(self, n: int) -> int:
        mod = 1000000007

        first = 1
        second = 1

        for _ in range(n):
            first, second = second, (first + second) % mod

        return second * second % mod
        
        

def main():
    sol = Solution()
    print(sol.countHousePlacements(1))
    print(sol.countHousePlacements(2))
    print(sol.countHousePlacements(8))

if __name__ == '__main__':
    main()