from typing import List

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        res_row = -1
        res_count = -1

        for index, row in enumerate(mat):
            cur_count = row.count(1)
            if cur_count > res_count:
                res_row = index
                res_count = cur_count
        
        return [res_row, res_count]
        
def main():
    sol = Solution()
    print(sol.rowAndMaximumOnes([[0,1],[1,0]]))
    print(sol.rowAndMaximumOnes([[0,0,0],[0,1,1]]))
    print(sol.rowAndMaximumOnes([[0,0],[1,1],[0,0]]))

if __name__ == '__main__':
    main()