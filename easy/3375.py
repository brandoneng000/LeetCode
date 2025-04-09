from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if min(nums) < k:
            return -1
        
        nums_set = set(nums)
        nums_set.discard(k)

        return len(nums_set)
        
def main():
    sol = Solution()
    print(sol.minOperations(nums = [5,2,5,4,5], k = 2))
    print(sol.minOperations(nums = [2,1,2], k = 2))
    print(sol.minOperations(nums = [9,7,5,3], k = 1))

if __name__ == '__main__':
    main()