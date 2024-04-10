from typing import List
from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        d = deque()

        for card in sorted(deck)[::-1]:
            d.rotate()
            d.appendleft(card)
        
        return d

    # def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
    #     deck.sort()
    #     n = len(deck)
    #     index = deque(range(n))
    #     res = [-1] * n

    #     for card in deck:
    #         res[index.popleft()] = card
    #         if index:
    #             index.append(index.popleft())

    #     return res
    
def main():
    sol = Solution()
    print(sol.deckRevealedIncreasing([17,13,11,2,3,5,7]))
    print(sol.deckRevealedIncreasing([1,1000]))

if __name__ == '__main__':
    main()