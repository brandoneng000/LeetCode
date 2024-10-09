class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_brackets = 0
        additional_brackets = 0

        for p in s:
            if p == '(':
                open_brackets += 1
            else:
                if open_brackets > 0:
                    open_brackets -= 1
                else:
                    additional_brackets += 1
            
        return open_brackets + additional_brackets

    # def minAddToMakeValid(self, s: str) -> int:
    #     stack = []

    #     for p in s:
    #         if stack and stack[-1] == '(' and p == ')':
    #             stack.pop()
    #         else:
    #             stack.append(p)
        
    #     return len(stack)

    # def minAddToMakeValid(self, s: str) -> int:
    #     stack = []

    #     for p in s:
    #         if p == "(":
    #             stack.append(p)
    #         elif not stack and p == ")":
    #             stack.append(")")
    #         elif stack[-1] == "(" and p == ")":
    #             stack.pop()
    #         else:
    #             stack.append(p)
        
    #     return len(stack)

def main():
    sol = Solution()
    print(sol.minAddToMakeValid("()))"))
    print(sol.minAddToMakeValid("())"))
    print(sol.minAddToMakeValid("((("))

if __name__ == '__main__':
    main()