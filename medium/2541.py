from typing import List

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if sum(nums1) != sum(nums2):
            return -1
        
        res = 0

        for i, j in zip(nums1, nums2):
            val = i - j
            if val and k == 0:
                return -1
            elif val > 0:
                quotient, remainder = divmod(val, k)
                if remainder:
                    return -1
                res += quotient
            elif val < 0:
                if val % k != 0:
                    return -1
        
        return res
        
def main():
    sol = Solution()
    print(sol.minOperations(nums1 = [4,3,1,4], nums2 = [1,3,7,1], k = 3))
    print(sol.minOperations(nums1 = [3,8,5,2], nums2 = [2,4,1,6], k = 1))

if __name__ == '__main__':
    main()