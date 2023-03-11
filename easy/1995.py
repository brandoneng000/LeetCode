from typing import List
import collections

class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        size = len(nums)
        result = 0
        count = collections.defaultdict(int)
        count[nums[size - 1] - nums[size - 2]] = 1
        
        for b in range(size - 3, 0, -1):
            for a in range(b - 1, -1, -1):
                result += count[nums[a] + nums[b]]
            
            for i in range(size - 1, b, -1):
                count[nums[i] - nums[b]] += 1

        return result
            

def main():
    sol = Solution()
    print(sol.countQuadruplets([1,2,3,6]))
    print(sol.countQuadruplets([3,3,6,4,5]))
    print(sol.countQuadruplets([1,1,1,3,5]))

if __name__ == '__main__':
    main()