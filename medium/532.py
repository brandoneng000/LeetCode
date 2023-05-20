from typing import List
import bisect
import collections

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        visited = set()
        count = collections.Counter(nums)

        for i in range(len(nums)):
            val1 = k - -nums[i]
            pair = (min(nums[i], val1), max(nums[i], val1))
            if val1 in count and pair not in visited:
                if val1 == nums[i] and count[val1] >= 2:
                    visited.add(pair)
                elif val1 != nums[i]:
                    visited.add(pair)

            val2 = nums[i] - k
            pair = (min(nums[i], val2), max(nums[i], val2))
            if val2 in count and pair not in visited:
                if val2 == nums[i] and count[val2] >= 2:
                    visited.add(pair)
                elif val2 != nums[i]:
                    visited.add(pair)
        
        return len(visited)

def main():
    sol = Solution()
    print(sol.findPairs(nums = [1,2,4,4,3,3,0,9,2,3], k = 3))
    print(sol.findPairs(nums = [3,1,4,1,5], k = 2))
    print(sol.findPairs(nums = [1,2,3,4,5], k = 1))
    print(sol.findPairs(nums = [1,3,1,5,4], k = 0))

if __name__ == '__main__':
    main()