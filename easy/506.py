from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        first = "Gold Medal"
        second = "Silver Medal"
        third = "Bronze Medal"
        ranks = {}
        scores = sorted(score, reverse=True)

        for index, s in enumerate(scores):
            if index == 0:
                ranks[s] = first
            elif index == 1:
                ranks[s] = second
            elif index == 2:
                ranks[s] = third
            else:
                ranks[s] = str(index + 1)
        
        results = []
        for s in score:
            results.append(ranks[s])
        return results

def main():
    sol = Solution()
    print(sol.findRelativeRanks([5, 4, 3, 2, 1]))
    print(sol.findRelativeRanks([10,3,8,9,4]))

if __name__ == '__main__':
    main()