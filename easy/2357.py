from typing import List
import heapq

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # nums = list(set([num for num in nums if num != 0]))
        # heapq.heapify(nums)
        # res = 0

        # while sum(nums):
        #     heapq.heappop(nums)
        #     res += 1
        
        # return res

        # nums = list(set([num for num in nums if num != 0]))
        # return len(nums)

        return len(set(nums) - {0})

def main():
    sol = Solution()
    print(sol.minimumOperations([1,5,0,3,5]))
    print(sol.minimumOperations([0]))

if __name__ == '__main__':
    main()