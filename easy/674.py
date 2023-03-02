from typing import List

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        length = 1
        max_length = 1

        for index in range(1, len(nums)):
            if nums[index - 1] < nums[index]:
                length += 1
                max_length = max(max_length, length)
            else:
                length = 1
        
        return max_length

def main():
    sol = Solution()
    print(sol.findLengthOfLCIS([1,3,5,4,7]))
    print(sol.findLengthOfLCIS([2,2,2,2,2]))

if __name__ == '__main__':
    main()