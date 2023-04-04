from typing import List
import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = collections.Counter(nums)
        keys = nums_count.keys()
        sorted_keys = sorted(keys, key=lambda x: nums_count[x], reverse=True)
        return sorted_keys[:k]


        
def main():
    sol = Solution()
    print(sol.topKFrequent(nums = [1,1,1,2,2,3], k = 2))
    print(sol.topKFrequent(nums = [1,1,1,2,2,3,4,4,4,4,4,4,4], k = 2))
    print(sol.topKFrequent(nums = [1], k = 1))

if __name__ == '__main__':
    main()