from typing import List

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        from collections import Counter

        total = Counter(s1.split())
        total.update(Counter(s2.split()))
        
        return [word for word in total if total[word] == 1]
        
def main():
    sol = Solution()
    print(sol.uncommonFromSentences("this apple is sweet", "this apple is sour"))

if __name__ == '__main__':
    main()