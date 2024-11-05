class Solution:
    def compressedString(self, word: str) -> str:
        res = [[0, word[0]]]

        for letter in word:
            if res[-1][1] == letter and res[-1][0] != 9:
                res[-1][0] += 1
            else:
                res.append([1, letter])
        
        return ''.join(str(count) + letter for count, letter in res)

def main():
    sol = Solution()
    print(sol.compressedString("abcde"))
    print(sol.compressedString("aaaaaaaaaaaaaabb"))

if __name__ == '__main__':
    main()