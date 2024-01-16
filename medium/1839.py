class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        res = 0
        vowels = "aeiou"
        index = 0
        cur_len = 0

        for c in word:
            if vowels[index] == c:
                cur_len += 1
            elif index < len(vowels) - 1 and vowels[index + 1] == c and cur_len > 0:
                cur_len += 1
                index += 1
            else:
                index = 0
                if vowels[index] == 'u':
                    res = max(res, cur_len)
                cur_len = 1 if vowels[index] == c else 0
            
            if vowels[index] == 'u':
                res = max(res, cur_len)
            
        return res

def main():
    sol = Solution()
    print(sol.longestBeautifulSubstring("aeiaaioaaaaeiiiiouuuooaauuaeiu"))
    print(sol.longestBeautifulSubstring("aeeeiiiioooauuuaeiou"))
    print(sol.longestBeautifulSubstring("a"))

if __name__ == '__main__':
    main()