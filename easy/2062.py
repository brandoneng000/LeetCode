import collections

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = "aeiou"
        result = 0
        vowel_count = collections.defaultdict(int)

        for index, letter in enumerate(word):
            if letter in vowels:
                if not index or word[index - 1] not in vowels: 
                    jj = j = index
                    vowel_count.clear()
                vowel_count[letter] += 1
                while len(vowel_count) == 5 and all(vowel_count.values()):
                    vowel_count[word[j]] -= 1
                    j += 1
                
                result += j - jj

        return result

def main():
    sol = Solution()
    print(sol.countVowelSubstrings("aeiouu"))
    print(sol.countVowelSubstrings("unicornarihan"))
    print(sol.countVowelSubstrings("cuaieuouac"))

if __name__ == '__main__':
    main()