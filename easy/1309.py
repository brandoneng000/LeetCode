class Solution:
    def freqAlphabets(self, s: str) -> str:
        dictionary_pre = {
            '1': 'a',
            '2': 'b',
            '3': 'c',
            '4': 'd',
            '5': 'e',
            '6': 'f',
            '7': 'g',
            '8': 'h',
            '9': 'i',
        }
        
        dictionary_latter = {
            '10#': 'j',
            '11#': 'k',
            '12#': 'l',
            '13#': 'm',
            '14#': 'n',
            '15#': 'o',
            '16#': 'p',
            '17#': 'q',
            '18#': 'r',
            '19#': 's',
            '20#': 't',
            '21#': 'u',
            '22#': 'v',
            '23#': 'w',
            '24#': 'x',
            '25#': 'y',
            '26#': 'z',
        }

        for letter in dictionary_latter:
            s = s.replace(letter, dictionary_latter[letter])

        for letter in dictionary_pre:
            s = s.replace(letter, dictionary_pre[letter])

        return s

        # for letter in 'abcdefghi':
        #     val = ord(letter) - ord('a') + 1
        #     print(f"'{val}': '{letter}',")
        
        # for letter in 'jklmnopqrstuvwxyz':
        #     val = ord(letter) - ord('a') + 1
        #     print(f"'{val}#': '{letter}',")

        
def main():
    sol = Solution()
    print(sol.freqAlphabets("10#11#12"))
    print(sol.freqAlphabets("1326#"))

if __name__ == '__main__':
    main()