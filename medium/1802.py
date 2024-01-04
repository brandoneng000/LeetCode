class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def test(a: int) -> int:
            b = max(a - index, 0)
            res = (a + b) * (a - b + 1) // 2
            b = max(a - ((n - 1) - index), 0)
            res += (a + b) * (a - b + 1) // 2
            return res - a
        
        maxSum -= n
        left, right = 0, maxSum

        while left < right:
            mid = (left + right + 1) // 2
            
            if test(mid) <= maxSum:
                left = mid
            else:
                right = mid - 1
        
        return left + 1
        
def main():
    sol = Solution()
    print(sol.maxValue(n = 4, index = 2,  maxSum = 6))
    print(sol.maxValue(n = 6, index = 1,  maxSum = 10))

if __name__ == '__main__':
    main()