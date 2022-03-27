from typing import List

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        from collections import Counter
        char_count = Counter(chars)
        res = []

        for word in words:
            word_count = Counter(word)
            res.append(word)
            for letter in word_count:
                if word_count[letter] > char_count[letter]:
                    res.remove(word)
                if word not in res:
                    break
        
        return sum([len(word) for word in res])

        
def main():
    sol = Solution()
    print(sol.countCharacters(["cat","bt","hat","tree"], "atach"))

if __name__ == '__main__':
    main()