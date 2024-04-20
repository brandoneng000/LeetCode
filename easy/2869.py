from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        k_vals = [False] * k
        res = 0

        for i in range(n - 1, -1, -1):
            res += 1

            if nums[i] - 1 < k:
                k_vals[nums[i] - 1] = True
            
            if all(k_vals):
                break
        
        return res
            


def main():
    sol = Solution()
    print(sol.minOperations(nums = [3,1,5,4,2], k = 2))
    print(sol.minOperations(nums = [3,1,5,4,2], k = 5))
    print(sol.minOperations(nums = [3,2,5,3,1], k = 3))

if __name__ == '__main__':
    main()