class Solution:
    def reformat(self, s: str) -> str:
        res = []
        letters = [letter for letter in s if letter.islower()]
        digits = [digit for digit in s if digit.isnumeric()]
        index_letters = 0
        index_digits = 0

        if abs(len(digits) - len(letters)) > 1:
            return ""

        while(index_letters < len(letters) and index_digits < len(digits)):
            res.append(letters[index_letters])
            res.append(digits[index_digits])
            index_letters += 1
            index_digits += 1

        if len(letters) > len(digits):
            res.append(letters[index_letters])
        elif len(digits) > len(letters):
            res.insert(0, digits[index_digits])

        return "".join(res)

def main():
    sol = Solution()
    print(sol.reformat("a0b1c2"))
    print(sol.reformat("a0b1c2aa"))
    print(sol.reformat("1a0b1c21"))
    print(sol.reformat("leetcode"))

if __name__ == '__main__':
    main()