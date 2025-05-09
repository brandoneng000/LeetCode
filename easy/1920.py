from typing import List

class Solution:
    # def buildArray(self, nums: List[int]) -> List[int]:
    #     n = len(nums)

    #     for i in range(n):
    #         nums[i] += 10000 * (nums[nums[i]] % 10000)
        
    #     for i in range(n):
    #         nums[i] //= 10000
        
    #     return nums

    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[nums[i]] for i in range(len(nums))]

    # def buildArray(self, nums: List[int]) -> List[int]:
    #     result = [None] * len(nums)
        
    #     for index in range(len(nums)):
    #         result[index] = nums[nums[index]]
        
    #     return result

    # def buildArray(self, nums: List[int]) -> List[int]:
    #     size = len(nums)

    #     for index in range(size):
    #         remainder = nums[index]
    #         product = nums[nums[index]] % size
    #         nums[index] = size * product + remainder
        
    #     for index in range(size):
    #         nums[index] //= size

    #     return nums

def main():
    sol = Solution()
    print(sol.buildArray([0,2,1,5,3,4]))
    print(sol.buildArray([5,0,1,2,3,4]))

if __name__ == '__main__':
    main()