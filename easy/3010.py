from typing import List

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        return nums[0] + sum(sorted(nums[1:])[:2])
        
def main():
    sol = Solution()
    print(sol.minimumCost([1,2,3,12]))
    print(sol.minimumCost([5,4,3]))
    print(sol.minimumCost([10,3,1,1]))

if __name__ == '__main__':
    main()