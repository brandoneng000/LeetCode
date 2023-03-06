from typing import List
import collections

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        deck_count = collections.Counter(deck)
        largest_set_deck = max(list(set(deck_count.values())))
        for denominator in range(2, largest_set_deck + 1):
            remainder = 0
            for count in deck_count.values():
                remainder += count % denominator
                if remainder != 0:
                    break
            if not remainder:
                return True
    
        return False

def main():
    sol = Solution()
    print(sol.hasGroupsSizeX([1,2,3,4,4,3,2,1]))
    print(sol.hasGroupsSizeX([1,1,1,2,2,2,3,3]))
    print(sol.hasGroupsSizeX([1]))
    print(sol.hasGroupsSizeX([1,1,2,2,2,2]))

if __name__ == '__main__':
    main()