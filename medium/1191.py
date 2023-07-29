from typing import List

class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        def helper(arr: List[int]):
            max_max = 0
            cur_max = 0

            for val in arr:
                cur_max = max(val, val + cur_max)
                max_max = max(max_max, cur_max)
            
            return max_max
        
        mod = 1000000007

        return ((k - 2) * max(sum(arr), 0) + helper(arr * 2)) % mod if k > 1 else helper(arr) % mod
        
        

def main():
    sol = Solution()
    print(sol.kConcatenationMaxSum(arr = [-5,-2,0,0,3,9,-2,-5,4], k = 5))
    print(sol.kConcatenationMaxSum(arr = [1,2], k = 3))
    print(sol.kConcatenationMaxSum(arr = [1,-2,1], k = 5))
    print(sol.kConcatenationMaxSum(arr = [-1,-2], k = 7))

if __name__ == '__main__':
    main()