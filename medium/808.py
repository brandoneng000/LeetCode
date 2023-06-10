class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 4500:
            return 1.0
        
        cache = {}
        def helper(a: int, b: int):
            if (a, b) in cache:
                return cache[(a, b)]
            
            if a <= 0 and b <= 0:
                return 0.5
            elif a <= 0:
                return 1.0
            elif b <= 0:
                return 0.0
            
            prob = (0.25) * (helper(a - 100, b) + helper(a - 75, b - 25) + helper(a - 50, b - 50) + helper(a - 25, b - 75))
            cache[(a, b)] = prob
            return cache[(a, b)]
        
        return helper(n, n)


def main():
    sol = Solution()
    print(sol.soupServings(50))
    print(sol.soupServings(100))

if __name__ == '__main__':
    main()