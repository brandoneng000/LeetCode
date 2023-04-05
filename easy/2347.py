from typing import List
import collections

class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        # if len(set(suits)) == 1:
        #     return "Flush"
        
        # cards = collections.Counter(ranks)
        # count = max(cards.values())

        # if count >= 3:
        #     return "Three of a Kind"
        # elif count == 2:
        #     return "Pair"
        # else:
        #     return "High Card"
        if len(set(suits)) == 1:
            return "Flush"
        
        cards = collections.Counter(ranks)

        if len(cards) <= 3 and max(cards.values()) >= 3:
            return "Three of a Kind"
        elif len(cards) <= 4:
            return "Pair"
        else:
            return "High Card"
        


def main():
    sol = Solution()
    print(sol.bestHand(ranks = [13,2,3,1,9], suits = ["a","a","a","a","a"]))
    print(sol.bestHand(ranks = [4,4,2,4,4], suits = ["d","a","a","b","c"]))
    print(sol.bestHand(ranks = [10,10,2,12,9], suits = ["a","b","c","a","d"]))

if __name__ == '__main__':
    main()