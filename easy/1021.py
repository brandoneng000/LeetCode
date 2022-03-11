class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        result = ""
        temp = ""

        for para in s:
            if para == "(":
                stack.append(para)
                temp += para
            else:
                stack.pop()
                temp += para

            if not stack:
                result += temp[1:-1]
                temp = ""

        return result

def main():
    sol = Solution()
    print(sol.removeOuterParentheses("(()())(())"))
    print(sol.removeOuterParentheses("(()())(())(()(()))"))

if __name__ == '__main__':
    main()