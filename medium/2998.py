class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        def dp(x: int, y: int):
            if x <= y:
                return y - x
            
            if x in cache:
                return cache[x]
            
            res = abs(x - y)
            res = min(res, 1 + x % 5 + dp(x // 5, y))
            res = min(res, 1 + (5 - x % 5) + dp(x // 5 + 1, y))
            res = min(res, 1 + x % 11 + dp(x // 11, y))
            res = min(res, 1 + (11 - x % 11) + dp(x // 11 + 1, y))

            cache[x] = res
            return cache[x]

        cache = {}
        return dp(x, y)

        

        
def main():
    sol = Solution()
    print(sol.minimumOperationsToMakeEqual(x = 26, y = 1))
    print(sol.minimumOperationsToMakeEqual(x = 54, y = 2))
    print(sol.minimumOperationsToMakeEqual(x = 25, y = 30))

if __name__ == '__main__':
    main()