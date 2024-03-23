from typing import List

class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        seen = set()

        for word in startWords:
            mask = 0
            for c in word:
                mask ^= 1 << ord(c) - 97
            seen.add(mask)
        
        res = 0

        for word in targetWords:
            mask = 0
            for c in word:
                mask ^= 1 << ord(c) - 97
            
            for c in word:
                if mask ^ (1 << ord(c) - 97) in seen:
                    res += 1
                    break
            
        return res



def main():
    sol = Solution()
    print(sol.wordCount(startWords = ["ant","act","tack"], targetWords = ["tack","act","acti"]))
    print(sol.wordCount(["ab","a"], targetWords = ["abc","abcd"]))

if __name__ == '__main__':
    main()