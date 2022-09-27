class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def letterToInt(word: str):
            temp = []

            for letter in word:
                temp.append(str(ord(letter) - ord('a')))

            return int("".join(temp))

        return letterToInt(firstWord) + letterToInt(secondWord) == letterToInt(targetWord)

        
def main():
    sol = Solution()
    print(sol.isSumEqual(firstWord = "acb", secondWord = "cba", targetWord = "cdb"))
    print(sol.isSumEqual(firstWord = "aaa", secondWord = "a", targetWord = "aab"))
    print(sol.isSumEqual(firstWord = "aaa", secondWord = "a", targetWord = "aaaa"))

if __name__ == '__main__':
    main()