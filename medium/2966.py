from typing import List

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        res = [[nums[i], nums[i + 1], nums[i + 2]] for i in range(0, len(nums), 3)]
        
        for group in res:
            if group[-1] - group[0] > k:
                return []

        return res

        
def main():
    sol = Solution()
    print(sol.divideArray(nums = [1,3,4,8,7,9,3,5,1], k = 2))
    print(sol.divideArray(nums = [1,3,3,2,7,3], k = 3))

if __name__ == '__main__':
    main()