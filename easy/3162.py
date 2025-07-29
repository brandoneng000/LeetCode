from typing import List

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n, m = len(nums1), len(nums2)
        res = 0

        for i in range(m):
            nums2[i] *= k

        for i in range(n):
            for j in range(m):
                res += nums1[i] % nums2[j] == 0
        
        return res
        
def main():
    sol = Solution()
    print(sol.numberOfPairs(nums1 = [1,3,4], nums2 = [1,3,4], k = 1))
    print(sol.numberOfPairs(nums1 = [1,2,4,12], nums2 = [2,4], k = 3))

if __name__ == '__main__':
    main()