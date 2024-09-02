from typing import List

class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        smallest = largest = 0

        for i in range(indexDifference, n):
            if nums[i - indexDifference] < nums[smallest]:
                smallest = i - indexDifference
            
            if nums[i - indexDifference] > nums[largest]:
                largest = i - indexDifference
            
            if nums[i] - nums[smallest] >= valueDifference:
                return [smallest, i]
            
            if nums[largest] - nums[i] >= valueDifference:
                return [largest, i]

        return [-1, -1]
        
def main():
    sol = Solution()
    print(sol.findIndices(nums = [5,1,4,1], indexDifference = 2, valueDifference = 4))
    print(sol.findIndices(nums = [2,1], indexDifference = 0, valueDifference = 0))
    print(sol.findIndices(nums = [1,2,3], indexDifference = 2, valueDifference = 4))

if __name__ == '__main__':
    main()