class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        return int(s.count(letter) / len(s) * 100)

def main():
    sol = Solution()
    print(sol.percentageLetter(s = "foobar", letter = "o"))
    print(sol.percentageLetter(s = "jjjj", letter = "k"))

if __name__ == '__main__':
    main()