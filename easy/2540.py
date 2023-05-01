from typing import List

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1

        return -1


    #     self.cache = set()

    #     for num in nums1:
    #         if num not in self.cache:
    #             if self.binary_search(nums2, num):
    #                 return num
    #         else:
    #             return num
        
    #     return -1
    
    # def binary_search(self, nums: List[int], goal: int) -> bool:
    #     left, right = 0, len(nums) - 1

    #     while left <= right:
    #         middle = (left + right) // 2
    #         self.cache.add(nums[middle])
    #         if nums[middle] == goal:
    #             return True
    #         elif nums[middle] < goal:
    #             left = middle + 1
    #         else:
    #             right = middle - 1
        
    #     return False

def main():
    sol = Solution()
    print(sol.getCommon(nums1 = [1,2,3], nums2 = [2,4]))
    print(sol.getCommon(nums1 = [1,2,3,6], nums2 = [2,3,4,5]))

if __name__ == '__main__':
    main()