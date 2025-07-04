class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def calc(x: int):
            if x < 0:
                return 0
            
            return x * (x - 1) // 2
        
        return calc(n + 2) - 3 * calc(n - limit + 1) + 3 * calc(n - (limit + 1) * 2 + 2) - calc(n - 3 * (limit + 1) + 2)


    # def distributeCandies(self, n: int, limit: int) -> int:
    #     if n > limit * 3:
    #         return 0

    #     res = 0

    #     for i in range(limit + 1):
    #         if n - i > limit * 2:
    #             continue
            
    #         j = n - i
    #         res += max(min(j, limit) - max(j - limit, 0) + 1, 0)
        
    #     return res
        
def main():
    sol = Solution()
    print(sol.distributeCandies(n = 5, limit = 2))
    print(sol.distributeCandies(n = 3, limit = 3))

if __name__ == '__main__':
    main()