from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if not nums:
        #     return 0

        # nums.sort()
        # longest = 1
        # count = 1
        # prev = nums[0]

        # for index in range(1, len(nums)):
        #     if prev + 1 == nums[index]:
        #         count += 1
        #     elif prev + 1 < nums[index]:
        #         count = 1

        #     prev = nums[index]
        #     longest = max(longest, count)

        # return longest

        nums = set(nums)
        longest = 0

        # looks along the set of numbers
        for x in nums:
            # goes through the set until you hit a number that lacks the preceding one
            # this means x will be the start of a continuous increase
            if x - 1 not in nums:
                y = x + 1
                # starts from x and starts incrementing until the consecutive increase stops
                while y in nums:
                    y += 1
                longest = max(longest, y - x)

        return longest

def main():
    sol = Solution()
    print(sol.longestConsecutive([100,4,200,1,3,2]))
    print(sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
    print(sol.longestConsecutive([1,2,0,1]))
    
if __name__ == '__main__':
    main()