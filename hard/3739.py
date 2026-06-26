from typing import List

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        prefix = [0] * (n * 2 + 1)
        prefix[n] = 1
        count = n
        res = presum = 0

        for i in range(n):
            if nums[i] == target:
                presum += prefix[count]
                count += 1
                prefix[count] += 1
            else:
                count -= 1
                presum -= prefix[count]
                prefix[count] += 1
            
            res += presum

        return res


def main():
    sol = Solution()
    print(sol.countMajoritySubarrays(nums = [1,2,2,3], target = 2))
    print(sol.countMajoritySubarrays(nums = [1,1,1,1], target = 1))
    print(sol.countMajoritySubarrays(nums = [1,2,3], target = 4))

if __name__ == '__main__':
    main()