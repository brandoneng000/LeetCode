from typing import List

class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        return max(max(left or [0]), n - min(right or [n]))
    
    # def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
    #     res = 0

    #     for l in left:
    #         res = max(res, l)
    #     for r in right:
    #         res = max(res, n - r)
        
    #     return res

    # def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
    #     return max(n - min(right) if right else 0, max(left) if left else 0)


        
def main():
    sol = Solution()
    print(sol.getLastMoment(n = 4, left = [4,3], right = [0,1]))
    print(sol.getLastMoment(n = 7, left = [], right = [0,1,2,3,4,5,6,7]))
    print(sol.getLastMoment(n = 7, left = [0,1,2,3,4,5,6,7], right = []))

if __name__ == '__main__':
    main()