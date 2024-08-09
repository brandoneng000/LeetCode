from typing import List
from collections import Counter

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        dominant, count = Counter(nums).most_common()[0]
        left, right = 0, count

        for i in range(n):
            if nums[i] == dominant:
                left += 1
                right -= 1
            if left * 2 > i + 1 and right * 2 > n - (i + 1):
                return i
        
        return -1


    # def minimumIndex(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     left = Counter()
    #     right = Counter(nums)

    #     for i in range(n):
    #         left[nums[i]] += 1
    #         right[nums[i]] -= 1
    #         left_common = left.most_common()[0]
    #         right_common = right.most_common()[0]

    #         if  left_common[1] * 2 > i + 1 and right_common[1] * 2 > n - (i + 1) and left_common[0] == right_common[0]:
    #             return i
        
    #     return -1


        
def main():
    sol = Solution()
    print(sol.minimumIndex([1,2,2,2]))
    print(sol.minimumIndex([2,1,3,1,1,1,7,1,2,1]))
    print(sol.minimumIndex([3,3,3,3,7,2,2]))

if __name__ == '__main__':
    main()