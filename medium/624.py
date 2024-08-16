from typing import List

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        n = len(arrays)
        first_max = [-float('inf'), -1]
        second_max = [-float('inf'), -1]
        first_min = [float('inf'), -1]
        second_min = [float('inf'), -1]
        res = -float('inf')
        
        for i in range(n):
            if arrays[i][-1] > first_max[0]:
                second_max = first_max
                first_max = [arrays[i][-1], i]
            elif arrays[i][-1] > second_max[0]:
                second_max = [arrays[i][-1], i]
            
            if arrays[i][0] < first_min[0]:
                second_min = first_min
                first_min = [arrays[i][0], i]
            elif arrays[i][0] < second_min[0]:
                second_min = [arrays[i][0], i]

        for max_num, i in [first_max, second_max]:
            for min_num, j in [first_min, second_min]:
                if i != j:
                    res = max(res, max_num - min_num)
        
        return res
        
        
def main():
    sol = Solution()
    print(sol.maxDistance([[1,2,3],[4,5],[1,2,3]]))
    print(sol.maxDistance([[1],[1]]))

if __name__ == '__main__':
    main()