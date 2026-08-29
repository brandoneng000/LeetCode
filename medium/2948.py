from typing import List
from collections import deque

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        nums_sorted = sorted(nums)

        curr_group = 0
        num_to_group = {}
        num_to_group[nums_sorted[0]] = curr_group

        group_to_list = {}
        group_to_list[curr_group] = deque([nums_sorted[0]])

        for i in range(1, n):
            if abs(nums_sorted[i] - nums_sorted[i - 1]) > limit:
                curr_group += 1

            num_to_group[nums_sorted[i]] = curr_group

            if curr_group not in group_to_list:
                group_to_list[curr_group] = deque()

            group_to_list[curr_group].append(nums_sorted[i])

        for i in range(n):
            num = nums[i]
            group = num_to_group[num]
            nums[i] = group_to_list[group].popleft()

        return nums

    # def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
    #     n = len(nums)
    #     nums_index = sorted([(nums[i], i) for i in range(n)])
    #     indexes = []
    #     res = [0] * n

    #     for i in range(n):
    #         if i == 0 or nums_index[i][0] - nums_index[i - 1][0] > limit:
    #             indexes.append([])
    #         indexes[-1].append(nums_index[i][1])
        
    #     for index in indexes:
    #         sorted_index = sorted(index)

    #         for j in range(len(sorted_index)):
    #             res[sorted_index[j]] = nums[index[j]]
        
    #     return res
        
def main():
    sol = Solution()
    print(sol.lexicographicallySmallestArray(nums = [1,5,3,9,8], limit = 2))
    print(sol.lexicographicallySmallestArray(nums = [1,7,6,18,2,1], limit = 3))
    print(sol.lexicographicallySmallestArray(nums = [1,7,28,19,10], limit = 3))

if __name__ == '__main__':
    main()