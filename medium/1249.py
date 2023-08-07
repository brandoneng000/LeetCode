class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        s_list = list(s)

        for i, c in enumerate(s_list):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if stack:
                    stack.pop()
                else:
                    s_list[i] = ''
        
        for i in stack:
            s_list[i] = ''
        
        return "".join(s_list)

    # def minRemoveToMakeValid(self, s: str) -> str:
    #     stack = [""]

    #     for c in s:
    #         if c == ')':
    #             if len(stack) > 1:
    #                 temp = '(' + stack.pop() + ')'
    #                 stack[-1] += temp
    #         elif c == '(':
    #             stack.append('')
    #         else:
    #             stack[-1] += c
        
    #     return ''.join(stack)

def main():
    sol = Solution()
    print(sol.minRemoveToMakeValid("lee(t(c)o)de)"))
    print(sol.minRemoveToMakeValid("a)b(c)d"))
    print(sol.minRemoveToMakeValid("))(("))

if __name__ == '__main__':
    main()