from collections import Counter
from string import ascii_lowercase

class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        count1, count2 = Counter(word1), Counter(word2)
        size1, size2 = len(count1), len(count2)

        for c1 in ascii_lowercase:
            for c2 in ascii_lowercase:
                if count1[c1] and count2[c2]:
                    if c1 == c2:
                        if size1 == size2:
                            return True
                    else:
                        temp1, temp2 = size1, size2
                        if count1[c1] == 1:
                            temp1 -= 1
                        if count1[c2] == 0:
                            temp1 += 1
                        if count2[c1] == 0:
                            temp2 += 1
                        if count2[c2] == 1:
                            temp2 -= 1
                        
                        if temp1 == temp2:
                            return True
        
        return False
        

        
def main():
    sol = Solution()
    print(sol.isItPossible(word1 = "ac", word2 = "b"))
    print(sol.isItPossible(word1 = "abcc", word2 = "aab"))
    print(sol.isItPossible(word1 = "abcde", word2 = "fghij"))

if __name__ == '__main__':
    main()