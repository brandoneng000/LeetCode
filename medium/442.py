from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []

        for n in nums:
            if nums[abs(n) - 1] < 0:
                res.append(abs(n))
            else:
                nums[abs(n) - 1] *= -1
        
        return res

def main():
    sol = Solution()
    print(sol.findDuplicates([4,3,2,7,8,2,3,1]))
    print(sol.findDuplicates(nums = [1,1,2]))
    print(sol.findDuplicates(nums = [1]))

if __name__ == '__main__':
    main()