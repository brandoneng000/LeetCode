from typing import List

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        mod = 1_000_000_007
        res = 0

        for l, r, k, v in queries:
            for i in range(l, r + 1, k):
                nums[i] = (nums[i] * v) % mod
            
        for num in nums:
            res ^= num
        
        return res

        
def main():
    sol = Solution()
    print(sol.xorAfterQueries(nums = [1,1,1], queries = [[0,2,1,4]]))
    print(sol.xorAfterQueries(nums = [2,3,1,5,4], queries = [[1,4,2,3],[0,2,1,2]]))

if __name__ == '__main__':
    main()