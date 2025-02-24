from typing import List

class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = [0] * (k + 2)

        for i in range(n // 2):
            left, right = nums[i], nums[n - i - 1]
            cur_diff = abs(right - left)
            max_diff = max(left, right, k - left, k - right)
            count[0] += 1
            count[cur_diff] -= 1
            count[cur_diff + 1] += 1
            count[max_diff + 1] += 1
        
        cur_changes = 0
        res = n

        for i in range(k + 1):
            cur_changes += count[i]
            res = min(res, cur_changes)

        return res

        
def main():
    sol = Solution()
    print(sol.minChanges(nums = [0,11,9,6,1,15,6,0,12,14], k = 15))
    print(sol.minChanges(nums = [1,0,1,2,4,3], k = 4))
    print(sol.minChanges(nums = [0,1,2,3,3,6,5,4], k = 6))

if __name__ == '__main__':
    main()