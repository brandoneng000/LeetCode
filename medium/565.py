from typing import List

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        res = 0
        visited = set()
        
        for i in range(len(nums)):
            cur = 1
            j = nums[i]
            while j != i and j not in visited:
                cur += 1
                visited.add(j)
                j = nums[j]
            res = max(res, cur)
        
        return res
            

def main():
    sol = Solution()
    print(sol.arrayNesting([5,4,0,3,1,6,2]))
    print(sol.arrayNesting([0,1,2]))

if __name__ == '__main__':
    main()