class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count_steps(n: int, left: int, right: int):
            steps = 0

            while left <= n:
                steps += min(n + 1, right) - left
                left *= 10
                right *= 10
            
            return steps
        
        res = 1
        k -= 1
        
        while k > 0:
            steps = count_steps(n, res, res + 1)

            if steps <= k:
                res += 1
                k -= steps
            else:
                res *= 10
                k -= 1
        
        return res
                
def main():
    sol = Solution()
    print(sol.findKthNumber(n = 1000000000, k = 1000000000))
    print(sol.findKthNumber(n = 1000000000, k = 1000000000 - 1))
    print(sol.findKthNumber(n = 13, k = 2))
    print(sol.findKthNumber(n = 1, k = 1))

if __name__ == '__main__':
    main()