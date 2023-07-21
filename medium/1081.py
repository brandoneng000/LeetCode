import bisect

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        letters = []
        string_index = { letter: index for index, letter in enumerate(s) }
        letter_check = set()

        for index, letter in enumerate(s):
            if letter in letter_check:
                continue
            while letters and letter < letters[-1] and index < string_index[letters[-1]]:
                letter_check.remove(letters.pop())
            
            letters.append(letter)
            letter_check.add(letter)
    
        return "".join(letters)

def main():
    sol = Solution()
    print(sol.smallestSubsequence("bcabc"))
    print(sol.smallestSubsequence("cbacdcbc"))

if __name__ == '__main__':
    main()