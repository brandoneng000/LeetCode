class Solution:
    def distMoney(self, money: int, children: int) -> int:
        money -= children
        if money < 0:
            return -1

        if (money // 7 == children and money % 7 == 0):
            return children
        
        if (money // 7 == children - 1 and money % 7 == 3):
            return children - 2
        
        return min(children - 1, money // 7)


def main():
    sol = Solution()
    print(sol.distMoney(money = 20, children = 3))
    print(sol.distMoney(money = 16, children = 2))

if __name__ == '__main__':
    main()