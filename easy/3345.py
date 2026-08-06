class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n, n + 1000):
            x = i
            pr = 1

            while x > 0:
                pr *= x % 10
                x //= 10

            if pr % t == 0:
                return i

    # def smallestNumber(self, n: int, t: int) -> int:
    #     def helper(n: int):
    #         res = 1

    #         while n:
    #             n, r = divmod(n, 10)
    #             res *= r
            
    #         return res
        
    #     res = n

    #     while helper(res) % t != 0:
    #         res += 1
        
    #     return res
        
def main():
    sol = Solution()
    print(sol.smallestNumber(n = 10, t = 2))
    print(sol.smallestNumber(n = 15, t = 3))

if __name__ == '__main__':
    main()