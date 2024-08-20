from typing import List
from collections import Counter

class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        n = len(nums)
        count = Counter(nums[:k])
        cur_sum = sum(nums[:k])
        res = 0 if len(count) < m else cur_sum
        left = 0

        for right in range(k, n):
            count[nums[left]] -= 1
            cur_sum -= nums[left]

            if count[nums[left]] == 0:
                count.pop(nums[left])
            
            count[nums[right]] += 1
            cur_sum += nums[right]

            if len(count) >= m and cur_sum > res:
                res = cur_sum

            left += 1
            right += 1
        
        return res


def main():
    sol = Solution()
    print(sol.maxSum(nums = [2,6,7,3,1,7], m = 3, k = 4))
    print(sol.maxSum(nums = [5,9,9,2,4,5,4], m = 1, k = 3))
    print(sol.maxSum(nums = [1,2,1,2,1,2,1], m = 3, k = 3))

if __name__ == '__main__':
    main()