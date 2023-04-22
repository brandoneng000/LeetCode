class Solution:
    def minTimeToType(self, word: str) -> int:
        res = len(word)
        cur_letter = 'a'

        for letter in word:
            res += min(abs(ord(letter) - ord(cur_letter)), 26 - abs(ord(letter) - ord(cur_letter)))
            cur_letter = letter
        
        return res

def main():
    sol = Solution()
    print(sol.minTimeToType("abc"))
    print(sol.minTimeToType("bza"))
    print(sol.minTimeToType("zjpc"))

if __name__ == '__main__':
    main()