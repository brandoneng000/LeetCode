class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        last_index = {}
        used = set()
        res = 0

        for index, letter in enumerate(s):
            last_index[letter] = index

        for index, letter in enumerate(s):
            if index != last_index[letter] and letter not in used:
                res += len(set(s[index + 1: last_index[letter]]))
                used.add(letter)
        
        return res
        
        
def main():
    sol = Solution()
    print(sol.countPalindromicSubsequence("aabca"))
    print(sol.countPalindromicSubsequence("adc"))
    print(sol.countPalindromicSubsequence("bbcbaba"))

if __name__ == '__main__':
    main()