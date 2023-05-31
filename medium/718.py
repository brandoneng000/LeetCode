from typing import List

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0 for i in range(len(nums2) + 1)] for j in range(len(nums1) + 1)]
        for i in range(len(nums1) - 1, -1, -1):
            for j in range(len(nums2) - 1, -1, -1):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1
        
        return max(max(row) for row in dp)

def main():
    sol = Solution()
    print(sol.findLength(nums1 = [0,1,1,1,1], nums2 = [1,0,1,0,1]))
    print(sol.findLength(nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]))
    print(sol.findLength(nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]))

if __name__ == '__main__':
    main()