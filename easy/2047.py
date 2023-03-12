class Solution:
    def countValidWords(self, sentence: str) -> int:
        sentence = sentence.split()
        result = 0

        for word in sentence:
            valid = True
            hyphen = 0
            for index, letter in enumerate(word):
                if letter.isdigit():
                    valid = False
                    break
                
                if (letter == '.' or letter == '!' or letter == ',') and index != len(word) - 1:
                    valid = False
                    break

                if letter == '-' and hyphen == 0:
                    hyphen += 1
                    if index - 1 < 0 or not word[index - 1].isalpha():
                        valid = False
                        break
                    if index + 1 >= len(word) or not word[index + 1].isalpha():
                        valid = False
                        break
                elif letter == '-' and hyphen == 1:
                    valid = False
                    break
            
            result += valid

        return result


def main():
    sol = Solution()
    print(sol.countValidWords("cat and  dog"))
    print(sol.countValidWords("!this  1-s b8d!"))
    print(sol.countValidWords("alice and  bob are playing stone-game10"))
    print(sol.countValidWords("he bought 2 pencils, 3 erasers, and 1  pencil-sharpener."))

if __name__ == '__main__':
    main()