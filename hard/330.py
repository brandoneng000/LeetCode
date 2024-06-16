from typing import List

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        covered = 0
        res = 0

        for num in nums:
            while num > covered + 1:
                res += 1
                covered = covered * 2 + 1
                if covered >= n:
                    return res
            
            covered += num

            if covered >= n:
                return res
        
        while covered < n:
            res += 1
            covered = covered * 2 + 1
        
        return res
        
def main():
    sol = Solution()
    print(sol.minPatches(nums = [1,3], n = 6))
    print(sol.minPatches(nums = [1,5,10], n = 20))
    print(sol.minPatches(nums = [1,2,2], n = 5))

if __name__ == '__main__':
    main()