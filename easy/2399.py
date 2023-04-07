from typing import List
import string

class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        letters = {}
        distance_dict = { letter: distance[i] for i, letter in enumerate(string.ascii_lowercase) }
        
        for index, letter in enumerate(s):
            letters[letter] = abs(index - letters.get(letter, 0))
        
        return all(letters[letter] - 1 == distance_dict[letter] for letter in letters)


def main():
    sol = Solution()
    print(sol.checkDistances(s = "abaccb", distance = [1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))
    print(sol.checkDistances(s = "aa", distance = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))

if __name__ == '__main__':
    main()