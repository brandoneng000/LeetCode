from typing import List
import heapq

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Odds are greater then adjacent evens
        """
        nums.sort()
        min_heap = nums[:len(nums) // 2 + 1]
        max_heap = [-n for n in nums[len(nums) // 2 - 1:]]
        heapq.heapify(min_heap)
        heapq.heapify(max_heap)
        start = len(nums) - 1 if (len(nums) - 1) % 2 == 0 else len(nums) - 2
        for i in range(start, -1, -2):
            nums[i] = heapq.heappop(min_heap)
        
        for i in range(1, len(nums), 2):
            nums[i] = -heapq.heappop(max_heap)


        

def main():
    sol = Solution()
    temp = [1,5,1,1,6,4]
    sol.wiggleSort(temp)
    print(temp)
    temp = [1,3,2,2,3,1]
    sol.wiggleSort(temp)
    print(temp)
    temp = [1,3,2,2,3,1,3]
    sol.wiggleSort(temp)
    print(temp)

if __name__ == '__main__':
    main()