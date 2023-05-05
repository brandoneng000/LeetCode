class Solution:
    def decodeString(self, s: str) -> str:
        res = ""
        stack = []
        stack_letters = []
        letters = ""
        num = 0

        for letter in s:
            if letter.isdigit():
                num = 10 * num + int(letter)
            elif letter == '[':
                stack.append(num)
                stack_letters.append(letters)
                letters = ""
                num = 0
            elif letter == ']':
                letters = stack_letters.pop() + (letters * stack.pop())
            else:
                letters += letter
            
            if not stack:
                res += letters
                letters = ""
        
        return res
            


def main():
    sol = Solution()
    print(sol.decodeString("3[a]2[bc]"))
    print(sol.decodeString("3[a2[c]]"))
    print(sol.decodeString("2[abc]3[cd]ef"))

if __name__ == '__main__':
    main()