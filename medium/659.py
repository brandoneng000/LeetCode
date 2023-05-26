from typing import List
import collections
import heapq

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        nums_list = collections.defaultdict(list)
        heapq.heapify(nums)
        
        for n in nums:
            if nums_list[n - 1]:
                heapq.heappush(nums_list[n], heapq.heappop(nums_list[n - 1]) + 1)
            else:
                heapq.heappush(nums_list[n], 1)
        
        return all(val > 2 for temp in nums_list for val in nums_list[temp])

def main():
    sol = Solution()
    print(sol.isPossible([1,2,3,3,4,5]))
    print(sol.isPossible([1,2,3,3,4,4,5,5]))
    print(sol.isPossible([1,2,3,4,4,5]))

if __name__ == '__main__':
    main()