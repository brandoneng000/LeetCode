from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # res = 1

        # nums = list(set(nums))
        # nums.sort()
        # while nums and nums[0] <= 0:
        #     nums.pop(0)

        # for index, num in enumerate(nums):
        #     if num != index + 1:
        #         return index + 1
        #     else:
        #         res = num + 1
        #     if num <= 0:
        #         return res
        
        # return res
        nums.append(0)
        size = len(nums)
        # removes all numbers less than 0 or greater than the size of the array
        for index in range(size):
            if nums[index] < 0 or nums[index] >= size:
                nums[index] = 0
        
        # increase nums[index] by size then use '%' to get original number
        for index in range(size):
            nums[nums[index] % size] += size

        for index in range(1, size):
            if nums[index] // size == 0:
                return index
        
        return size

def main():
    sol = Solution()
    print(sol.firstMissingPositive([1,2,0,0,0,0]))
    print(sol.firstMissingPositive([3,4,-1,1]))
    print(sol.firstMissingPositive([-1]))
    print(sol.firstMissingPositive([1, 1000]))
    print(sol.firstMissingPositive([2, 2]))

if __name__ == '__main__':
    main()
