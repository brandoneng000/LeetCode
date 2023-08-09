from typing import List

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        n = len(nums)

        def valid_pairs(threshold: int):
            index = 0
            count = 0

            while index < n - 1:
                if nums[index + 1] - nums[index] <= threshold:
                    count += 1
                    index += 1
                index += 1
            
            return count

        left, right = 0, nums[-1] - nums[0]
        while left < right:
            middle = (left + right) // 2

            if valid_pairs(middle) >= p:
                right = middle
            else:
                left = middle + 1

        return left

def main():
    sol = Solution()
    print(sol.minimizeMax(nums = [10,1,2,7,1,3], p = 2))
    print(sol.minimizeMax(nums = [4,2,1,2], p = 1))

if __name__ == '__main__':
    main()