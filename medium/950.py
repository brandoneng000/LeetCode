from typing import List
import collections

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        index = collections.deque(range(len(deck)))
        res = [None] * len(deck)

        for card in deck:
            res[index.popleft()] = card
            if index:
                index.append(index.popleft())

        return res
    
def main():
    sol = Solution()
    print(sol.deckRevealedIncreasing([17,13,11,2,3,5,7]))
    print(sol.deckRevealedIncreasing([1,1000]))

if __name__ == '__main__':
    main()