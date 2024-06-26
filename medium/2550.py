class Solution:
    def monkeyMove(self, n: int) -> int:
        mod = 1000000007
        return (pow(2, n, mod) - 2) % mod

    # def monkeyMove(self, n: int) -> int:
    #     mod = 1000000007
    #     res = 6
    #     n -= 3

    #     while n:
    #         res = ((res * 2) + 2) % mod
    #         n -= 1
        
    #     return res
        

def main():
    sol = Solution()
    print(sol.monkeyMove(3))
    print(sol.monkeyMove(4))

if __name__ == '__main__':
    main()