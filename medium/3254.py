from typing import List

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = []
        cur = -1
        count = 0

        for i in range(k - 1):
            if cur + 1 == nums[i]:
                count += 1
            else:
                count = 1

            cur = nums[i]

        for i in range(k - 1, n):
            if cur + 1 == nums[i]:
                count += 1
            else:
                count = 1

            cur = nums[i]
            
            if count >= k:
                res.append(nums[i])
            else:
                res.append(-1)
        
        return res

        
def main():
    sol = Solution()
    print(sol.resultsArray(nums = [1,2,3,4,3,2,5], k = 3))
    print(sol.resultsArray(nums = [2,2,2,2,2], k = 4))
    print(sol.resultsArray(nums = [3,2,3,2,3,2], k = 2))

if __name__ == '__main__':
    main()