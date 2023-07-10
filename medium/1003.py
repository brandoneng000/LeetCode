class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for letter in s:
            if letter == 'c':
                if stack[-2:] != ['a', 'b']:
                    return False
                stack.pop()
                stack.pop()
            else:
                stack.append(letter)

        return not stack
    
    # def isValid(self, s: str) -> bool:
    #     while 'abc' in s:
    #         s = s.replace('abc', '')
        
    #     return s == ''

def main():
    sol = Solution()
    print(sol.isValid("aabcbc"))
    print(sol.isValid("abcabcababcc"))
    print(sol.isValid("abccba"))

if __name__ == '__main__':
    main()