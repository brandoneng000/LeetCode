class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        def helper_and(index: int):
            state = True
            skip = -1

            for i in range(index + 2, open_brace_end[index + 1]):
                if i < skip:
                    continue

                if expression[i] == '&':
                    state &= helper_and(i)
                    skip = open_brace_end[i + 1]
                elif expression[i] == '|':
                    state &= helper_or(i)
                    skip = open_brace_end[i + 1]
                elif expression[i] == '!':
                    state &= helper_not(i)
                    skip = open_brace_end[i + 1]
                elif expression[i] == 'f':
                    state = False
                
                if not state:
                    break
            
            return state

        def helper_or(index: int):
            state = False
            skip = -1

            for i in range(index + 2, open_brace_end[index + 1]):
                if i < skip:
                    continue

                if expression[i] == '&':
                    state |= helper_and(i)
                    skip = open_brace_end[i + 1]
                elif expression[i] == '|':
                    state |= helper_or(i)
                    skip = open_brace_end[i + 1]
                elif expression[i] == '!':
                    state |= helper_not(i)
                    skip = open_brace_end[i + 1]
                elif expression[i] == 't':
                    state = True
                
                if state:
                    break
            
            return state

        def helper_not(index: int):
            for i in range(index + 2, open_brace_end[index + 1]):
                if expression[i] == '&':
                    return not helper_and(i)
                elif expression[i] == '|':
                    return not helper_or(i)
                elif expression[i] == '!':
                    return not helper_not(i)
                elif expression[i] == 't':
                    return False
                elif expression[i] == 'f':
                    return True


        n = len(expression)
        open_brace_end = {}
        stack = []

        for i in range(n):
            if expression[i] == '(':
                stack.append(i)
            elif expression[i] == ')':
                open_brace_end[stack.pop()] = i
        
        if expression[0] == 't':
            return True
        elif expression[0] == 'f':
            return False
        elif expression[0] == '&':
            return helper_and(0)
        elif expression[0] == '|':
            return helper_or(0)
        elif expression[0] == '!':
            return helper_not(0)

        
def main():
    sol = Solution()
    print(sol.parseBoolExpr("!(&(!(&(f)),&(t),|(f,f,t)))"))
    print(sol.parseBoolExpr("!(&(!(t),&(f),|(f)))"))
    print(sol.parseBoolExpr("&(|(f))"))
    print(sol.parseBoolExpr("|(f,f,f,t)"))
    print(sol.parseBoolExpr("!(&(f,t))"))

if __name__ == '__main__':
    main()