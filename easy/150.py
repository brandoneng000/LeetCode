from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == '+':
                val_first = stack.pop()
                val_second = stack.pop()
                stack.append(val_second + val_first)
            elif token == '-':
                val_first = stack.pop()
                val_second = stack.pop()
                stack.append(val_second - val_first)
            elif token == '*':
                val_first = stack.pop()
                val_second = stack.pop()
                stack.append(val_second * val_first)
            elif token == '/':
                val_first = stack.pop()
                val_second = stack.pop()
                stack.append(int(val_second / val_first))
            else:
                stack.append(int(token))
        
        return stack.pop()

def main():
    sol = Solution()
    print(sol.evalRPN(["2","1","+","3","*"]))
    print(sol.evalRPN(["4","13","5","/","+"]))
    print(sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
    print(sol.evalRPN(["10","6","9","3","+","11","*","/","*","17","+","5","+"]))

if __name__ == '__main__':
    main()