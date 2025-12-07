class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high + 1) // 2 - (low // 2)

    # def countOdds(self, low: int, high: int) -> int:
    #     result = high % 2 == 1 or low % 2 == 1
    #     result += (high - low) // 2
    #     return result

def main():
    sol = Solution()
    print(sol.countOdds(3, 7))
    print(sol.countOdds(8, 10))

if __name__ == '__main__':
    main()