from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        res = float('inf')
        
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    for k in range(j + 1, n):
                        if nums[k] < nums[j]:
                            res = min(res, nums[i] + nums[j] + nums[k])
        
        return res if res != float('inf') else -1


def main():
    sol = Solution()
    print(sol.minimumSum([8,6,1,5,3]))
    print(sol.minimumSum([5,4,8,7,10,2]))
    print(sol.minimumSum([6,5,4,3,4,5]))

if __name__ == '__main__':
    main()