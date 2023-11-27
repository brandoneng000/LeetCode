from typing import List

class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        mod = 1000000007
        n = len(nums)
        prefix = nums.copy()
        j = k = 0
        res = 0

        for i in range(1, n):
            prefix[i] += prefix[i - 1]
        
        for i in range(n - 2):
            while j <= i or (j < n - 1 and prefix[j] < prefix[i] * 2):
                j += 1
            while k < j or (k < n - 1 and prefix[k] - prefix[i] <= prefix[-1] - prefix[k]):
                k += 1
            res = (res + k - j) % mod
        
        return res
        
        
def main():
    sol = Solution()
    print(sol.waysToSplit([1,1,1]))
    print(sol.waysToSplit([1,2,2,2,5,0]))
    print(sol.waysToSplit([3,2,1]))

if __name__ == '__main__':
    main()