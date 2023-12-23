from typing import List

class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        m = len(nums)
        i = 0

        for g in groups:
            while i < m:
                if nums[i: i + len(g)] == g:
                    i += len(g)
                    break
                else:
                    i += 1
            else:
                return False
        
        return True


        
def main():
    sol = Solution()
    print(sol.canChoose( groups = [[1,-1,-1],[3,-2,0]], nums = [1,-1,0,1,-1,-1,3,-2,0]))
    print(sol.canChoose(groups = [[10,-2],[1,2,3,4]], nums = [1,2,3,4,10,-2]))
    print(sol.canChoose(groups = [[1,2,3],[3,4]], nums = [7,7,1,2,3,4,7,7]))

if __name__ == '__main__':
    main()