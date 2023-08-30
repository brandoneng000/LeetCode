from typing import List

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        res = 0

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                continue

            num_elements = (nums[i] + nums[i + 1] - 1) // nums[i + 1]

            res += num_elements - 1

            nums[i] = nums[i] // num_elements
    
        return res



def main():
    sol = Solution()
    print(sol.minimumReplacement([3,9,3]))
    print(sol.minimumReplacement([1,2,3,4,5]))

if __name__ == '__main__':
    main()