class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def check_vowels(vowels: dict):
            return all(vowels[v] > 0 for v in vowels)

        def helper(word: str, k: int):
            n = len(word)
            left = 0
            vowels = { 'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0 }
            consonants = 0
            res = 0

            for right in range(n):
                if word[right] not in vowels:
                    consonants += 1
                else:
                    vowels[word[right]] += 1
                
                while consonants >= k and check_vowels(vowels):
                    res += n - right

                    if word[left] not in vowels:
                        consonants -= 1
                    else:
                        vowels[word[left]] -= 1

                    left += 1
            
            return res
        
        return helper(word, k) - helper(word, k + 1)

        
def main():
    sol = Solution()
    print(sol.countOfSubstrings(word = "aeioqq", k = 1))
    print(sol.countOfSubstrings(word = "aeiou", k = 0))
    print(sol.countOfSubstrings(word = "ieaouqqieaouqq", k = 1))

if __name__ == '__main__':
    main()