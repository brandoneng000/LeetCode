from typing import List

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        res = [-1] * len(nums)
        cur_sum = sum(nums[0: k + k + 1])
        size = k + k + 1

        for i in range(k, len(nums) - k):
            res[i] = cur_sum // size
            cur_sum -= nums[i - k]
            if i + k + 1 < len(nums):
                cur_sum += nums[i + k + 1]
        
        return res

def main():
    sol = Solution()
    print(sol.getAverages(nums = [7,4,3,9,1,8,5,2,6], k = 3))
    print(sol.getAverages(nums = [100000], k = 0))
    print(sol.getAverages(nums = [8], k = 100000))

if __name__ == '__main__':
    main()