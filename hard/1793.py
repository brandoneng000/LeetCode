from typing import List

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = k
        right = k
        res = nums[k]
        cur_min = nums[k]

        while left > 0 or right < n - 1:
            if (nums[left - 1] if left else 0) < (nums[right + 1] if right < n - 1 else 0):
                right += 1
                cur_min = min(cur_min, nums[right])
            else:
                left -= 1
                cur_min = min(cur_min, nums[left])
            
            res = max(res, cur_min * (right - left + 1))
        
        return res


def main():
    sol = Solution()
    print(sol.maximumScore(nums = [1,4,3,7,4,5], k = 3))
    print(sol.maximumScore(nums = [5,5,4,5,4,1,1,1], k = 0))

if __name__ == '__main__':
    main()