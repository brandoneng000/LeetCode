class Solution:
    def clumsy(self, n: int) -> int:
        if n < 3:
            return n
        elif n == 3:
            return 6
        elif n == 4:
            return 7
        else:
            remainder = n % 4
            if remainder == 0:
                return n + 1
            elif remainder <= 2:
                return n + 2
            else:
                return n - 1

    # def clumsy(self, n: int) -> int:
    #     equation = [str(n)]

    #     for val in range(1, n):
    #         remainder = val % 4
    #         if remainder == 1:
    #             equation.append(f'*{n - val}')
    #         elif remainder == 2:
    #             equation.append(f'//{n - val}')
    #         elif remainder == 3:
    #             equation.append(f'+{n - val}')
    #         else:
    #             equation.append(f'-{n - val}')
        
    #     return eval("".join(equation))

    # def clumsy(self, n: int) -> int:
    #     stack = [n]

    #     for val in range(1, n):
    #         remainder = val % 4
    #         if remainder == 1:
    #             stack[-1] = stack[-1] * (n - val)
    #         elif remainder == 2:
    #             stack[-1] = stack[-1] // (n - val) if stack[-1] > 0 else -(-stack[-1] // (n - val))
    #         elif remainder == 3:
    #             stack.append(n - val)
    #         else:
    #             stack.append(-(n - val))

    #     return sum(stack)


def main():
    sol = Solution()
    print(sol.clumsy(4))
    print(sol.clumsy(10))

if __name__ == '__main__':
    main()