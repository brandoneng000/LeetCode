from typing import List

class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        for i in range(n):
            for j in range(i, n):
                prev = -1
                flag = True

                for k in range(n):
                    if i <= k <= j:
                        continue
                    if prev >= nums[k]:
                        flag = False
                        break
                    prev = nums[k]
                if flag:
                    res += 1
        
        return res
        
def main():
    sol = Solution()
    print(sol.incremovableSubarrayCount([1,2,3,4]))
    print(sol.incremovableSubarrayCount([6,5,7,8]))
    print(sol.incremovableSubarrayCount([8,7,6,6]))

if __name__ == '__main__':
    main()