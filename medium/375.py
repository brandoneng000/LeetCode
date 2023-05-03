class Solution:
    def getMoneyAmount(self, n: int) -> int:
        cache = {}
        
        def helper(start: int, end: int):
            if start >= end:
                return 0
            if (start, end) in cache:
                return cache[(start, end)]
            
            res = float('inf')
            for pick in range(start, end + 1):
                res = min(res, pick + max(helper(start, pick - 1), helper(pick + 1, end)))
        
            cache[(start, end)] = res
            return res
        
        return helper(1, n)


def main():
    sol = Solution()
    print(sol.getMoneyAmount(10))
    print(sol.getMoneyAmount(1))
    print(sol.getMoneyAmount(2))

if __name__ == '__main__':
    main()