from typing import List

class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        knew = k - 1

        if knew == 0:
            return True
        
        for i in range(k + 1, n):
            if nums[i] > nums[i - 1] and nums[i - k] > nums[i - k - 1]:
                knew -= 1
            else:
                knew = k - 1
            
            if knew == 0:
                return True
        
        return False

        
def main():
    sol = Solution()
    print(sol.hasIncreasingSubarrays(nums = [2,5,7,8,9,2,3,4,3,1], k = 3))
    print(sol.hasIncreasingSubarrays(nums = [1,2,3,4,4,4,4,5,6,7], k = 5))

if __name__ == '__main__':
    main()