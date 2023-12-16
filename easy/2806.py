class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        rounded = (purchaseAmount + 5) // 10

        return 100 - (rounded * 10)
        
def main():
    sol = Solution()
    print(sol.accountBalanceAfterPurchase(9))
    print(sol.accountBalanceAfterPurchase(15))

if __name__ == '__main__':
    main()