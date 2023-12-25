from typing import List
from collections import Counter

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)

        if m > n * 6 or n > m * 6:
            return -1

        
        total1, total2 = sum(nums1), sum(nums2)
        if total1 > total2:
            return self.minOperations(nums2, nums1)
        
        count = Counter(6 - n for n in nums1)
        count += Counter(n - 1 for n in nums2)
        i = 5
        res = 0

        while total2 > total1:
            while count[i] == 0:
                i -= 1
            total1 += i
            count[i] -= 1
            res += 1
        
        return res
        
def main():
    sol = Solution()
    print(sol.minOperations(nums1 = [1,2,3,4,5,6], nums2 = [1,1,2,2,2,2]))
    print(sol.minOperations(nums1 = [1,1,1,1,1,1,1], nums2 = [6]))
    print(sol.minOperations(nums1 = [6,6], nums2 = [1]))

if __name__ == '__main__':
    main()