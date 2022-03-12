class Solution:
    def intToRoman(self, num: int) -> str:
        roman = { 1000: "M", 500: "D", 100: "C", 50: "L", 10: "X", 5: "V", 1: "I" }
        roman_numeral = ""

        for rom in roman:
            while num >= rom:
                num -= rom
                roman_numeral += roman[rom]

            if (num >= 900 and rom == 1000) or (num >= 400 and rom == 500):
                num -= rom - 100
                roman_numeral += "C" + roman[rom]
            if (num >= 90 and rom == 100) or (num >= 40 and rom == 50):
                num -= rom - 10
                roman_numeral += "X" + roman[rom]
            if (num >= 9 and rom == 10) or (num >= 4 and rom == 5):
                num -= rom - 1
                roman_numeral += "I" + roman[rom]

        return roman_numeral

def main():
    sol = Solution()
    print(sol.intToRoman(3900))
    print(sol.intToRoman(3))
    print(sol.intToRoman(58))
    print(sol.intToRoman(1994))

if __name__ == '__main__':
    main()