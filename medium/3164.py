from typing import List
from collections import Counter
from math import isqrt

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums2 = [num * k for num in nums2]
        nums1_count = Counter(nums1)
        nums2_count = Counter(nums2)
        factors = Counter()
        res = 0

        for num in nums1_count:
            for i in range(1, isqrt(num) + 1):
                if i * i == num:
                    factors[i] += nums1_count[num]
                elif num % i == 0:
                    factors[i] += nums1_count[num]
                    factors[num // i] += nums1_count[num]
        
        for num in nums2_count:
            res += factors[num] * nums2_count[num]

        return res

        
def main():
    sol = Solution()
    print(sol.numberOfPairs(nums1 = [1,3,4], nums2 = [1,3,4], k = 1))
    print(sol.numberOfPairs(nums1 = [1,2,4,12], nums2 = [2,4], k = 3))

if __name__ == '__main__':
    main()