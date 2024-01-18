from typing import List

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        i = 0

        for j, b in enumerate(nums2):
            while i < len(nums1) and nums1[i] > b:
                i += 1
            if i == len(nums1):
                break

            res = max(res, j - i)
        
        return res
        
def main():
    sol = Solution()
    print(sol.maxDistance(nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5]))
    print(sol.maxDistance(nums1 = [2,2,2], nums2 = [10,10,1]))
    print(sol.maxDistance(nums1 = [30,29,19,5], nums2 = [25,25,25,25,25]))

if __name__ == '__main__':
    main()