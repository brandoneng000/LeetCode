from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        bottom = [0] * (len(triangle[-1]) + 1)

        for row in range(len(triangle) - 1, -1, -1):
            for index in range(len(triangle[row])):
                triangle[row][index] = triangle[row][index] + min(bottom[index], bottom[index + 1])
            bottom = triangle[row]
        
        return triangle[0][0]

        


def main():
    sol = Solution()
    print(sol.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
    print(sol.minimumTotal([[-10]]))

if __name__ == '__main__':
    main()