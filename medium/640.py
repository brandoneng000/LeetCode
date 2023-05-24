class Solution:
    def solveEquation(self, equation: str) -> str:
        left, right = equation.split("=")
        left_vals = self.parse_side(left)
        right_vals = self.parse_side(right)
        x = left_vals[0] - right_vals[0]
        constant = right_vals[1] - left_vals[1]
        if x == 0 and constant:
            return "No solution"
        elif x == 0 and not constant:
            return "Infinite solutions"
        return f"x={constant // x}"

    def parse_side(self, side: str):
        vals = [0, 0]
        temp = ""
        variable = 1
        for i in range(len(side) - 1, -1, -1):
            if side[i] == 'x':
                variable = 0
            elif side[i] == '-':
                if not variable and not temp:
                    temp = '1'
                vals[variable] -= int(temp)
                temp = ""
                variable = 1
            elif side[i] == '+':
                if not variable and not temp:
                    temp = '1'
                vals[variable] += int(temp)
                temp = ""
                variable = 1
            else:
                temp = side[i] + temp
        
        if temp or not variable:
            if not variable and not temp:
                temp = '1'
            vals[variable] += int(temp)
        
        return vals
                

def main():
    sol = Solution()
    print(sol.solveEquation("x+5-3+x=6+x-2"))
    print(sol.solveEquation("x=x"))
    print(sol.solveEquation("2x=x"))

if __name__ == '__main__':
    main()