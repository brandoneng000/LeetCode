class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        stars = []
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if stack:
                    stack.pop()
                elif stars:
                    stars.pop()
                else:
                    return False
            else:
                stars.append(i)
        
        while stack and stars:
            if stack.pop() > stars.pop():
                return False
        
        return not stack

    # def checkValidString(self, s: str) -> bool:
    #     stack = []
    #     left_para_index = []
    #     for c in s:
    #         if c == '(':
    #             left_para_index.append(len(stack))
    #             stack.append(c)
    #         elif c == '*':
    #             stack.append(c)
    #         else:
    #             if stack:
    #                 if stack[-1] == '(':
    #                     stack.pop()
    #                     left_para_index.pop()
    #                 elif left_para_index:
    #                     stack.pop(left_para_index.pop())
    #                 elif stack[-1] == '*':
    #                     stack.pop()
    #                 else:
    #                     return False
    #             else:
    #                 return False

    #     stars = 0
    #     while stack:
    #         temp = stack.pop()
    #         if temp == '*':
    #             stars += 1
    #         elif temp == '(' and stars:
    #             stars -= 1
    #         else:
    #             return False
        
    #     return not stack
                    
        

def main():
    sol = Solution()
    print(sol.checkValidString("()"))
    print(sol.checkValidString("(*)"))
    print(sol.checkValidString("(*))"))

if __name__ == '__main__':
    main()