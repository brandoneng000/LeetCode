from typing import List

class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while(len(nums) != 1):
            new_nums = [0] * (len(nums) // 2)
            for index in range(len(new_nums)):
                if index % 2:
                    new_nums[index] = max(nums[2 * index], nums[2 * index + 1])
                else:
                    new_nums[index] = min(nums[2 * index], nums[2 * index + 1])
            nums = new_nums

        return nums.pop()


def main():
    sol = Solution()
    print(sol.minMaxGame([1,3,5,2,4,8,2,2]))
    print(sol.minMaxGame([3]))

if __name__ == '__main__':
    main()