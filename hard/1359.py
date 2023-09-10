class Solution:
    def countOrders(self, n: int) -> int:
        mod = 1000000007
        res = 1

        for i in range(2, n + 1):
            res = res * (i * 2 - 1) * (i * 2) // 2 % mod
        
        return res

def main():
    sol = Solution()
    print(sol.countOrders(1))
    print(sol.countOrders(2))
    print(sol.countOrders(3))

if __name__ == '__main__':
    main()