from typing import List
from collections import Counter

class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        count_letter = Counter(c for word in words for c in word)
        length_words = sorted(len(word) for word in words)
        res = 0

        for size in length_words:
            if size % 2:
                for c in count_letter:
                    if count_letter[c] % 2 == 1:
                        size -= 1
                        count_letter[c] -= 1
                        break
                else:
                    for c in count_letter:
                        if count_letter[c] > 0:
                            count_letter[c] -= 1
                            size -= 1
                            break
            
            for c in count_letter:
                if size > count_letter[c] - count_letter[c] % 2:
                    size -= count_letter[c] - count_letter[c] % 2
                    count_letter[c] -= count_letter[c] - count_letter[c] % 2
                else:
                    count_letter[c] -= size
                    size = 0
                    break
                
            if size == 0:
                res += 1
        
        return res
        
def main():
    sol = Solution()
    print(sol.maxPalindromesAfterOperations(words = ["ad","chahc","ccd"]))
    print(sol.maxPalindromesAfterOperations(words = ["abbb","ba","aa"]))
    print(sol.maxPalindromesAfterOperations(words = ["abc","ab"]))
    print(sol.maxPalindromesAfterOperations(words = ["cd","ef","a"]))

if __name__ == '__main__':
    main()