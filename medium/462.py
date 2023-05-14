from typing import List

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        start, end = 0, len(nums) - 1
        res = 0
        while start < end:
            res += nums[end] - nums[start]
            start += 1
            end -= 1
        
        return res

def main():
    sol = Solution()
    print(sol.minMoves2([1,0,0,8,6]))
    print(sol.minMoves2([1,2,3]))
    print(sol.minMoves2([1,10,2,9]))

if __name__ == '__main__':
    main()