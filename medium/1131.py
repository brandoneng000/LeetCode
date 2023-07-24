from typing import List

class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        res = 0
        n = len(arr1)
        
        for p, q in [[1, 1], [1, -1], [-1, 1], [-1, -1]]:
            smallest = p * arr1[0] + q * arr2[0] + 0
            for i in range(n):
                cur = p * arr1[i] + q * arr2[i] + i
                res = max(res, cur - smallest)
                smallest = min(smallest, cur)
        
        return res

def main():
    sol = Solution()
    print(sol.maxAbsValExpr(arr1 = [1,2,3,4], arr2 = [-1,4,5,6]))
    print(sol.maxAbsValExpr(arr1 = [1,-2,-5,0,10], arr2 = [0,-2,-1,-7,-4]))

if __name__ == '__main__':
    main()