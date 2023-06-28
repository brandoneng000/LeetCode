class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []

        for p in s:
            if p == "(":
                stack.append(p)
            elif not stack and p == ")":
                stack.append(")")
            elif stack[-1] == "(" and p == ")":
                stack.pop()
            else:
                stack.append(p)
        
        return len(stack)

def main():
    sol = Solution()
    print(sol.minAddToMakeValid("()))"))
    print(sol.minAddToMakeValid("())"))
    print(sol.minAddToMakeValid("((("))

if __name__ == '__main__':
    main()