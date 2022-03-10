class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = "aeiouAEIOU"
        words = sentence.split()
        goat = []

        for index, word in enumerate(words):
            if word[0] not in vowels:
                word = word[1:] + word[0]
            word += "ma" + "a" * (index + 1)
            goat.append(word)
        
        return " ".join(goat)
        
def main():
    sol = Solution()
    print(sol.toGoatLatin("I speak Goat Latin"))

if __name__ == '__main__':
    main()