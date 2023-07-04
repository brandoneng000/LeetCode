from typing import List

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def remove_vowel(word: str):
            return "".join('*' if c in 'aeiou' else c for c in word)
        
        def solve(query: str):
            if query in words_exact:
                return query
            
            query_lower = query.lower()

            if query_lower in words_cap:
                return words_cap[query_lower]
            
            query_vowel = remove_vowel(query_lower)
            
            if query_vowel in words_vow:
                return words_vow[query_vowel]
            
            return ""

        words_exact = set(wordlist)
        words_cap = {}
        words_vow = {}

        for word in wordlist:
            word_lower = word.lower()
            words_cap.setdefault(word_lower, word)
            words_vow.setdefault(remove_vowel(word_lower), word)
        
        return map(solve, queries)


def main():
    sol = Solution()
    print(sol.spellchecker(["hello"], ["hello", "hell"]))
    print(sol.spellchecker(wordlist = ["KiTe","kite","hare","Hare"], queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]))
    print(sol.spellchecker(wordlist = ["yellow"], queries = ["YellOw"]))

if __name__ == '__main__':
    main()