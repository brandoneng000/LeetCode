from typing import List
from collections import Counter

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        town = Counter()
        judge = set(range(1, n + 1))

        for a, b in trust:
            town[b] += 1
            judge.discard(a)

        for j in judge:
            if town[j] == n - 1:
                return j
        
        return -1


    # def findJudge(self, n: int, trust: List[List[int]]) -> int:
    #     from collections import defaultdict
    #     town = defaultdict(list)
    #     judge_trust = set([ppl for ppl in range(1, n + 1)])

    #     for t in trust:
    #         town[t[1]].append(t[0])
    #         if t[0] in judge_trust:
    #             judge_trust.remove(t[0])
            
    #     for judge in judge_trust:
    #         if len(town[judge]) == n - 1:
    #             return judge

    #     return -1

def main():
    sol = Solution()
    print(sol.findJudge(n = 2, trust = [[1,2]]))
    print(sol.findJudge(n = 3, trust = [[1,3],[2,3]]))
    print(sol.findJudge(n = 3, trust = [[1,3],[2,3],[3,1]]))

if __name__ == '__main__':
    main()