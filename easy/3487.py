from typing import List

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        res = set()

        for num in nums:
            if num > 0:
                res.add(num)
        
        return sum(res) if res else max(nums)
        
def main():
    sol = Solution()
    print(sol.maxSum([1,2,3,4,5]))
    print(sol.maxSum([1,1,0,1,1]))
    print(sol.maxSum([1,2,-1,-2,1,0,-1]))

if __name__ == '__main__':
    main()