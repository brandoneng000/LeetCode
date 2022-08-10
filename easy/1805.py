import string


class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        for letter in string.ascii_lowercase:
            word = word.replace(letter, ' ')
        
        word = list(set(word.strip().split(' ')))
        word = [int(num) for num in word if num != '']
        
        return len(set(word))


def main():
    sol = Solution()
    print(sol.numDifferentIntegers("a123bc34d8ef34"))
    print(sol.numDifferentIntegers("leet1234code234"))
    print(sol.numDifferentIntegers("a1b01c001"))

if __name__ == '__main__':
    main()