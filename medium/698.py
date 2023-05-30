from typing import List

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)

        if total % k != 0:
            return False
        subset_sum = total // k
        subsets = [0] * k
        nums.sort(reverse=True)
        
        def helper(i: int):
            if i == len(nums):
                return True
            
            for j in range(k):
                if subsets[j] + nums[i] <= subset_sum:
                    subsets[j] += nums[i]

                    if helper(i + 1):
                        return True
                    subsets[j] -= nums[i]

                    if subsets[j] == 0:
                        break
            return False

        return helper(0)
        
def main():
    sol = Solution()
    print(sol.canPartitionKSubsets(nums = [4,3,2,3,5,2,1], k = 4))
    print(sol.canPartitionKSubsets(nums = [1,2,3,4], k = 3))

if __name__ == '__main__':
    main()