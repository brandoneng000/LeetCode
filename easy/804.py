from typing import List

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        from string import ascii_lowercase as lower

        coded_word = ""
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..",
            "--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        codes = dict(zip(list(lower), morse))
        morse_codes = {}

        for word in words:
            for letter in word:
                coded_word += codes[letter]
            morse_codes[word] = coded_word
            coded_word = ""

        return len(set(morse_codes.values()))

def main():
    sol = Solution()
    print(sol.uniqueMorseRepresentations(["gin","zen","gig","msg"]))
    print(sol.uniqueMorseRepresentations(["a"]))

if __name__ == '__main__':
    main()