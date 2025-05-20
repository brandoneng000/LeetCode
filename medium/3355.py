from typing import List

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        prefix = [0] * (n + 1)
        cur = 0

        for l, r in queries:
            prefix[l] += 1
            prefix[r + 1] -= 1

        for i in range(n):
            cur += prefix[i]
            
            if nums[i] > cur:
                return False
        
        return True
    
        
def main():
    sol = Solution()
    print(sol.isZeroArray(nums = [1,0,1], queries = [[0,2]]))
    print(sol.isZeroArray(nums = [4,3,2,1], queries = [[1,3],[0,2]]))

if __name__ == '__main__':
    main()