from typing import List

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        licensePlate = licensePlate.lower()
        letters = {}
        dictionary = {}
        res = []

        for letter in licensePlate:
            if letter.isalpha():
                if letter in letters:
                    letters[letter] += 1
                else:
                    letters[letter] = 1

        for word in words:
            dictionary[word] = 0
            for letter in letters:
                if letter in word:
                    dictionary[word] += min(letters[letter], word.count(letter))

        matching = max(dictionary.values())
        for word in dictionary:
            if dictionary[word] == matching:
                res.append(word)
        
        return min(res, key=len)
        

def main():
    sol = Solution()
    print(sol.shortestCompletingWord("1s3 PSt", ["step","steps", "stips","stripe","stepple"]))
    print(sol.shortestCompletingWord("1s3 456", ["looks","pest","stew","show"]))


if __name__ == '__main__':
    main()