from typing import List

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        nums_dict = {}

        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if r - c not in nums_dict:
                    nums_dict[r - c] = val
                elif nums_dict[r - c] != val:
                    return False
        
        return True
        


def main():
    sol = Solution()
    print(sol.isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))
    print(sol.isToeplitzMatrix([[1,2],[2,2]]))
    print(sol.isToeplitzMatrix([[19,67,6,70,19]]))

if __name__ == '__main__':
    main()