from typing import List

class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        n = len(nums)

        if n == 1 and k % 2 == 1:
            return -1
        
        cur_max = -1
        
        for i in range(min(n, k - 1)):
            cur_max = max(cur_max, nums[i])
        
        if k < n:
            cur_max = max(cur_max, nums[k])
        
        return cur_max

        
def main():
    sol = Solution()
    print(sol.maximumTop(nums = [5,2,2,4,0,6], k = 4))
    print(sol.maximumTop(nums = [2], k = 1))

if __name__ == '__main__':
    main()