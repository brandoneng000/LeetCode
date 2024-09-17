from typing import List
from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        return [w for w, c in Counter(s1.split() + s2.split()).items() if c == 1]

    # def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
    #     count = Counter(s1.split() + s2.split())
    #     return [w for w, c in count.items() if c == 1]

    # def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
    #     from collections import Counter

    #     total = Counter(s1.split())
    #     total.update(Counter(s2.split()))
        
    #     return [word for word in total if total[word] == 1]
        
def main():
    sol = Solution()
    print(sol.uncommonFromSentences("this apple is sweet", "this apple is sour"))
    print(sol.uncommonFromSentences(s1 = "apple apple", s2 = "banana"))

if __name__ == '__main__':
    main()