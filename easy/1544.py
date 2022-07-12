class Solution:
    def makeGood(self, s: str) -> str:
        if not s: return ""
        
        stack = []
        stack.append(s[0])

        for index in range(1, len(s)):
            if stack and abs(ord(s[index]) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(s[index])
        
        return "".join(stack)



def main():
    sol = Solution()
    print(sol.makeGood("leEeetcode"))
    print(sol.makeGood("abBAcC"))
    print(sol.makeGood(""))

if __name__ == '__main__':
    main()