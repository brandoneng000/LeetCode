class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text = text.split()
        result = len(text)

        for word in text:
            for broken in brokenLetters:
                if broken in word:
                    result -= 1
                    break
        
        return result



def main():
    sol = Solution()
    print(sol.canBeTypedWords(text = "hello world", brokenLetters = "ad"))
    print(sol.canBeTypedWords(text = "leet code", brokenLetters = "lt"))
    print(sol.canBeTypedWords(text = "leet code", brokenLetters = "e"))

if __name__ == '__main__':
    main()