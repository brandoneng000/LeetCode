class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        if len(s) <= 2:
            return 0
        
        letters = set(s)
        res = 0

        for letter in letters:
            left = s.find(letter)
            right = s.rfind(letter)

            if left != right:
                res += len(set(s[left + 1: right]))
        
        return res

    # def countPalindromicSubsequence(self, s: str) -> int:
    #     last_index = {}
    #     used = set()
    #     res = 0

    #     for index, letter in enumerate(s):
    #         last_index[letter] = index

    #     for index, letter in enumerate(s):
    #         if index != last_index[letter] and letter not in used:
    #             res += len(set(s[index + 1: last_index[letter]]))
    #             used.add(letter)
        
    #     return res
        
        
def main():
    sol = Solution()
    print(sol.countPalindromicSubsequence("aabca"))
    print(sol.countPalindromicSubsequence("adc"))
    print(sol.countPalindromicSubsequence("bbcbaba"))

if __name__ == '__main__':
    main()