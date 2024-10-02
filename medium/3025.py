from typing import List

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        res = 0

        for i in range(n):
            for j in range(n):

                if i != j and points[i][0] <= points[j][0] and points[i][1] >= points[j][1]:
                    
                    for k in range(n):
                        if i == k or j == k:
                            continue

                        if points[i][0] <= points[k][0] <= points[j][0] and points[i][1] >= points[k][1] >= points[j][1]:
                            break
                    else:
                        res += 1
        
        return res
        
def main():
    sol = Solution()
    print(sol.numberOfPairs([[1,1],[2,2],[3,3]]))
    print(sol.numberOfPairs([[6,2],[4,4],[2,6]]))
    print(sol.numberOfPairs([[3,1],[1,3],[1,1]]))

if __name__ == '__main__':
    main()