class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # if ch not in word:
        #     return word
        # prefix = list(word[:word.index(ch) + 1])
        # prefix.reverse()
        # return "".join(prefix) + word[word.index(ch) + 1:]
        if ch not in word:
            return word
        
        return word[:word.find(ch) + 1][::-1] + word[word.find(ch) + 1:]

def main():
    sol = Solution()
    print(sol.reversePrefix(word = "abcdefd", ch = "d"))
    print(sol.reversePrefix(word = "xyxzxe", ch = "z"))
    print(sol.reversePrefix(word = "abcd", ch = "z"))

if __name__ == '__main__':
    main()