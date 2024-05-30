from typing import List

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        res = 0

        if m % 2:
            for num in nums2:
                res ^= num
        
        if n % 2:
            for num in nums1:
                res ^= num
        
        return res
        
def main():
    sol = Solution()
    print(sol.xorAllNums(nums1 = [2,1,3], nums2 = [10,2,5,0]))
    print(sol.xorAllNums(nums1 = [1,2], nums2 = [3,4]))

if __name__ == '__main__':
    main()