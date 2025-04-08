from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        seen = set()

        for i in range(n - 1, -1, -1):
            if nums[i] in seen:
                return i // 3 + 1
            seen.add(nums[i])
        
        return 0

    # def minimumOperations(self, nums: List[int]) -> int:
    #     res = 0

    #     while nums and len(set(nums)) != len(nums):
    #         nums = nums[3:]
    #         res += 1

    #     return res
        
        
def main():
    sol = Solution()
    print(sol.minimumOperations([1,2,3,4,2,3,3,5,7]))
    print(sol.minimumOperations([4,5,6,4,4]))
    print(sol.minimumOperations([6,7,8,9]))

if __name__ == '__main__':
    main()