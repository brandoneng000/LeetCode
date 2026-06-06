class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def helper(n: int):
            res = 1

            while n:
                n, r = divmod(n, 10)
                res *= r
            
            return res
        
        res = n

        while helper(res) % t != 0:
            res += 1
        
        return res
        
def main():
    sol = Solution()
    print(sol.smallestNumber(n = 10, t = 2))
    print(sol.smallestNumber(n = 15, t = 3))

if __name__ == '__main__':
    main()