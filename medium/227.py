class Solution:
    def calculate(self, s: str) -> int:
        # s = s.replace(' ', '')
        # s = s.replace('-', '+-')
        # if s[0] == '+':
        #     s = s.replace('+', '', 1)
        
        # def run_two_operations(op1, op2, s):
        #     while op1 in s or op2 in s:
        #         op1_index = float('inf') if s.find(op1) == -1 else s.find(op1)
        #         op2_index = float('inf') if s.find(op2) == -1 else s.find(op2)
        #         cur_op = min(op1_index, op2_index)
        #         num1 = ''
        #         num2 = ''
        #         val = ''
        #         index = cur_op - 1
        #         while index >= 0 and s[index] not in '+/*':
        #             num1 = s[index] + num1
        #             index -= 1
        #         index = cur_op + 1
        #         while index < len(s) and s[index] not in '+/*':
        #             num2 += s[index]
        #             index += 1
        #         if s[cur_op] == '*':
        #             val = str(int(num1) * int(num2))
        #         elif s[cur_op] == '/':
        #             val = str(int(int(num1) / int(num2)))
        #         elif s[cur_op] == '+':
        #             val = str(int(num1) + int(num2))
        #         s = s.replace(f'{num1}{s[cur_op]}{num2}', val, 1)
            
        #     return s
        
        # s = run_two_operations('*', '/', s)
        # s = run_two_operations('+', '?', s)
        # return int(s)
        if not s:
            return 0
        stack = []
        cur_num = 0
        operation = '+'
        for index, c in enumerate(s):
            if c.isdigit():
                cur_num = (cur_num * 10) + int(c)
            if not c.isdigit() and c != ' ' or index == len(s) - 1:
                if operation == '-':
                    stack.append(-cur_num)
                elif operation == '+':
                    stack.append(cur_num)
                elif operation == '*':
                    stack.append(stack.pop() * cur_num)
                elif operation == '/':
                    stack.append(int(stack.pop() / cur_num))
                operation = c
                cur_num = 0

        return sum(stack)

def main():
    sol = Solution()
    print(sol.calculate("3+2*2"))
    print(sol.calculate(" 3/2 "))
    print(sol.calculate(" 3+5 / 2 "))
    print(sol.calculate("0-2147483647"))
    print(sol.calculate("-2*2"))
    print(sol.calculate("14-3/2"))
    print(sol.calculate("700+2122-1047+1*2*21*2*2*2*2+1*10*4/4/2*2*3*3*8"))
    print(sol.calculate(""))

if __name__ == '__main__':
    main()