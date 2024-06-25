from typing import List

class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        score.sort(key=lambda x: x[k], reverse=True)

        return score

    # def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
    #     n = len(score)
    #     vals = sorted([(score[i][k], i) for i in range(n)], reverse=True)

    #     return [score[i] for _, i in vals]
        
def main():
    sol = Solution()
    print(sol.sortTheStudents(score = [[10,6,9,1],[7,5,11,2],[4,8,3,15]], k = 2))
    print(sol.sortTheStudents(score = [[3,4],[5,6]], k = 0))

if __name__ == '__main__':
    main()