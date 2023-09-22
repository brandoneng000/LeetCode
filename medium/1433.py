from typing import Counter
import collections
from string import ascii_lowercase

class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        def helper(count1: Counter, count2: Counter):
            s = 0

            for letter in ascii_lowercase:
                s += count1[letter] - count2[letter]
                if s < 0:
                    return False
            
            return True
        
        count1 = collections.Counter(s1)
        count2 = collections.Counter(s2)

        return helper(count1, count2) or helper(count2, count1)


    # def checkIfCanBreak(self, s1: str, s2: str) -> bool:
    #     check1 = []
    #     check2 = []

    #     for x, y in zip(sorted(s1), sorted(s2)):
    #         check1.append(x >= y)
    #         check2.append(y >= x)

    #     return all(check1) or all(check2)
        
def main():
    sol = Solution()
    print(sol.checkIfCanBreak(s1 = "abc", s2 = "xya"))
    print(sol.checkIfCanBreak(s1 = "abe", s2 = "acd"))
    print(sol.checkIfCanBreak(s1 = "leetcodee", s2 = "interview"))

if __name__ == '__main__':
    main()