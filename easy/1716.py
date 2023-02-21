class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        days = n % 7

        # weekly income is 28 + additional money per week
        money = weeks * 28
        money += weeks * (weeks - 1) * 7 // 2
        money += days * (days - 1) // 2 + (weeks + 1) * days

        return money

def main():
    sol = Solution()
    # print(sol.totalMoney(2))
    # print(sol.totalMoney(14))
    # print(sol.totalMoney(21))
    print(sol.totalMoney(4))
    print(sol.totalMoney(10))
    print(sol.totalMoney(20))
    print(sol.totalMoney(1000))

if __name__ == '__main__':
    main()