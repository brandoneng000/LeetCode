from typing import List

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        points.sort(key=lambda x: (x[0], -x[1]))
        res = 0

        for i in range(n):
            x1, y1 = points[i]
            y = -float('inf')

            for j in range(i + 1, n):
                x2, y2 = points[j]

                if y < y2 <= y1:
                    res += 1
                    y = points[j][1]
        
        return res
    
    # def numberOfPairs(self, points: List[List[int]]) -> int:
    #     n = len(points)
    #     points.sort(key=lambda x: (-x[0], x[1]))
    #     res = 0

    #     for i in range(n):
    #         _, bottom = points[i]
    #         top = 1 << 31

    #         for j in range(i + 1, n):
    #             if bottom <= points[j][1] < top:
    #                 res += 1
    #                 top = points[j][1]

    #                 if bottom == top:
    #                     break
        
    #     return res

def main():
    sol = Solution()
    print(sol.numberOfPairs([[1,1],[2,2],[3,3]]))
    print(sol.numberOfPairs([[6,2],[4,4],[2,6]]))
    print(sol.numberOfPairs([[3,1],[1,3],[1,1]]))

if __name__ == '__main__':
    main()