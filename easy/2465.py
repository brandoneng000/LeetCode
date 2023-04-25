from typing import List
import heapq

class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        negative_nums = [-n for n in nums]
        heapq.heapify(nums)
        heapq.heapify(negative_nums)
        count = len(nums) // 2
        averages = set()

        while count:
            count -= 1
            averages.add((-heapq.heappop(negative_nums) + heapq.heappop(nums)) / 2)
        
        return len(averages)
        

def main():
    sol = Solution()
    print(sol.distinctAverages([4,1,4,0,3,5]))
    print(sol.distinctAverages([1,100]))

if __name__ == '__main__':
    main()