from typing import List
from collections import Counter

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = set()
        losses = Counter()
        single_loss = []

        for w, l in matches:
            winners.add(w)
            losses[l] += 1
        
        for l in losses:
            winners.discard(l)

            if losses[l] == 1:
                single_loss.append(l)
        
        return [sorted(winners), sorted(single_loss)]
        
def main():
    sol = Solution()
    print(sol.findWinners(matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]))
    print(sol.findWinners(matches = [[2,3],[1,3],[5,4],[6,4]]))

if __name__ == '__main__':
    main()