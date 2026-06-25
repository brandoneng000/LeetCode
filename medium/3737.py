from typing import List

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        res = 0

        for i in range(n):
            count = 0
            size = 0

            for j in range(i, n):
                if nums[j] == target:
                    count += 1
                
                size += 1

                if count > size // 2:
                    res += 1
        
        return res


def main():
    sol = Solution()
    print(sol.countMajoritySubarrays(nums = [1,2,2,3], target = 2))
    print(sol.countMajoritySubarrays(nums = [1,1,1,1], target = 1))
    print(sol.countMajoritySubarrays(nums = [1,2,3], target = 4))

if __name__ == '__main__':
    main()