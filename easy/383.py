class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = {}

        for letter in magazine:
            if letter in mag:
                mag[letter] += 1
            else:
                mag[letter] = 1

        for letter in ransomNote:
            if letter in mag and mag[letter] > 0:
                mag[letter] -= 1
            else:
                return False
        
        return True
        
        # if len(ransomNote) > len(magazine):
        #     return False
        
        # ransom = list(ransomNote)
        # mag = list(magazine)

        # for letter in ransom:
        #     if letter in mag:
        #         mag.remove(letter)
        #     else:
        #         return False
        
        # return True


        
def main():
    sol = Solution()
    print(sol.canConstruct("a", "b"))
    print(sol.canConstruct("a", "ab"))
    print(sol.canConstruct("aa", "ab"))
    print(sol.canConstruct("aa", "aab"))

if __name__ == '__main__':
    main()