from string import ascii_lowercase

class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        n = len(word)
        word_list = list(word)
        letters = { letter:i for i, letter in enumerate(ascii_lowercase) }
        letters['A'] = 10000
        res = 0

        for i in range(n - 1):
            if word_list[i] == word_list[i + 1] or letters[word_list[i]] == (letters[word_list[i + 1]] - 1) or letters[word_list[i]] == (letters[word_list[i + 1]] + 1):
                word_list[i + 1] = 'A'
                res += 1
        
        return res

        
def main():
    sol = Solution()
    print(sol.removeAlmostEqualCharacters("aaaaa"))
    print(sol.removeAlmostEqualCharacters("abddez"))
    print(sol.removeAlmostEqualCharacters("zyxyxyz"))

if __name__ == '__main__':
    main()