from typing import List

class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        n = len(edges)
        res = -1
        max_score = 0
        score = [0] * n

        for i, num in enumerate(edges):
            score[num] += i

        for i in range(n):
            if score[i] > max_score:
                max_score = score[i]
                res = i
        
        return res

        
def main():
    sol = Solution()
    print(sol.edgeScore([1,0,0,0,0,7,7,5]))
    print(sol.edgeScore([2,0,0,2]))

if __name__ == '__main__':
    main()