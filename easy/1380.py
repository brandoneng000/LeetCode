from typing import List

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        min_nums = []
        result = []
        transpose = list(zip(*matrix))
        # transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

        for row in matrix:
            smallest_in_row = min(row)
            index_small = row.index(smallest_in_row)
            min_nums.append((smallest_in_row, index_small))

        for nums in min_nums:
            if nums[0] == max(transpose[nums[1]]):
                result.append(nums[0])
        
        return result
        

def main():
    sol = Solution()
    print(sol.luckyNumbers([[3,7,8],[9,11,13],[15,16,17]]))
    print(sol.luckyNumbers([[1,10,4,2],[9,3,8,7],[15,16,17,12]]))
    print(sol.luckyNumbers([[7,8],[1,2]]))

if __name__ == '__main__':
    main()