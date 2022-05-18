class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:

        for index, word in enumerate(sentence.split()):
            if word[:len(searchWord)] == searchWord:
                return index + 1
        
        return -1

        
def main():
    sol = Solution()
    print(sol.isPrefixOfWord("i love eating burger", "burg"))
    print(sol.isPrefixOfWord("this problem is an easy problem", "pro"))
    print(sol.isPrefixOfWord("i am tired", "you"))
    print(sol.isPrefixOfWord("hellohello hellohellohello", "ell"))

if __name__ == '__main__':
    main()