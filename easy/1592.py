class Solution:
    def reorderSpaces(self, text: str) -> str:
        spaces = text.count(' ')
        words = text.split()
        if spaces == 0:
            return text
        if len(words) == 1:
            return "".join(words) + (" " * spaces)
        extra_spaces = spaces % (len(words) - 1)
        spaces -= extra_spaces
        spaces = " " * (spaces // (len(words) - 1))
        res = spaces.join(words)
        return res + (" " * extra_spaces)

        
def main():
    sol = Solution()
    print(sol.reorderSpaces("  this   is  a sentence "))
    print(sol.reorderSpaces(" practice   makes   perfect"))
    print(sol.reorderSpaces("a"))
    print(sol.reorderSpaces("   a"))

if __name__ == '__main__':
    main()