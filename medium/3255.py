from typing import List

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = []
        cur_count = 0

        for i in range(n):
            if nums[i - 1] < nums[i] and nums[i - 1] + 1 == nums[i]:
                cur_count += 1
            else:
                cur_count = 1

            if cur_count >= k:
                res.append(nums[i])
            else:
                res.append(-1)
        
        return res[k - 1:]

        
def main():
    sol = Solution()
    print(sol.resultsArray(nums = [1,2,3,4,3,2,5], k = 3))
    print(sol.resultsArray(nums = [2,2,2,2,2], k = 4))
    print(sol.resultsArray(nums = [3,2,3,2,3,2], k = 2))

if __name__ == '__main__':
    main()