from typing import List

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        size1, size2 = len(nums1), len(nums2)
        dp = [[-float('inf') for _ in range(size2 + 1)] for _ in range(size1 + 1)]
        
        for i in range(size1 + 1):
            for j in range(size2 + 1):
                if i == 0 or j == 0:
                    continue
                dot = nums1[i - 1] * nums2[j - 1]
                dp[i][j] = max(dot, dp[i - 1][j - 1] + dot, dp[i - 1][j], dp[i][j - 1])

        return dp[size1][size2]

        

def main():
    sol = Solution()
    print(sol.maxDotProduct(nums1 = [2,1,-2,5], nums2 = [3,0,-6]))
    print(sol.maxDotProduct(nums1 = [3,-2], nums2 = [2,-6,7]))
    print(sol.maxDotProduct(nums1 = [-1,-1], nums2 = [1,1]))

if __name__ == '__main__':
    main()