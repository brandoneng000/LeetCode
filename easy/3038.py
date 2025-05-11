from typing import List

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)
        res = 1
        score = nums[0] + nums[1]

        for i in range(2, n - 1, 2):
            if nums[i] + nums[i + 1] == score:
                res += 1
            else:
                break
        
        return res
        
def main():
    sol = Solution()
    print(sol.maxOperations([3,2,1,4,5]))
    print(sol.maxOperations([1,5,3,3,4,1,3,2,2,3]))
    print(sol.maxOperations([5,3]))

if __name__ == '__main__':
    main()