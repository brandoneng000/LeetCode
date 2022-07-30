class Solution:
    def interpret(self, command: str) -> str:
        # res = ""
        # index, end = 0, len(command)

        # while index < end:
        #     if command[index] == 'G':
        #         res += 'G'
        #     else:
        #         if command[index + 1] == ')':
        #             res += 'o'
        #         else:
        #             res += 'al'
        #             index += 2
        #         index += 1
        #     index += 1

        # return res

        return command.replace('()', 'o').replace('(al)', 'al')

        
def main():
    sol = Solution()
    print(sol.interpret("G()(al)"))
    print(sol.interpret("G()()()()(al)"))
    print(sol.interpret("(al)G(al)()()G"))

if __name__ == '__main__':
    main()