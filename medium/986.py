from typing import List

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        index1 = 0
        index2 = 0
        m, n = len(firstList), len(secondList)

        while index1 < m and index2 < n:
            start = max(firstList[index1][0], secondList[index2][0])
            end = min(firstList[index1][1], secondList[index2][1])
            if start <= end:
                res.append([start, end])
            
            if firstList[index1][1] < secondList[index2][1]:
                index1 += 1
            else:
                index2 += 1
        
        return res
        

def main():
    sol = Solution()
    print(sol.intervalIntersection(firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]))
    print(sol.intervalIntersection(firstList = [[1,3],[5,9]], secondList = []))

if __name__ == '__main__':
    main()