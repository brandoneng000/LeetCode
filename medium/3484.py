# param_3 = obj.getValue(formula)
class Spreadsheet:
    def get_coords(self, cell: str):
        col = ord(cell[0]) - ord('A')
        row = int(cell[1:]) - 1

        return (row, col)

    def __init__(self, rows: int):
        self.excel = [[0] * 26 for _ in range(rows)]

    def setCell(self, cell: str, value: int) -> None:
        row, col = self.get_coords(cell)
        self.excel[row][col] = value

    def resetCell(self, cell: str) -> None:
        row, col = self.get_coords(cell)
        self.excel[row][col] = 0

    def getValue(self, formula: str) -> int:
        formula = formula[1:]
        left, right = formula.split('+')
        res = 0

        if not left.isdigit():
            row, col = self.get_coords(left)
            res += self.excel[row][col]
        else:
            res += int(left)

        if not right.isdigit():
            row, col = self.get_coords(right)
            res += self.excel[row][col]
        else:
            res += int(right)
        
        return res


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)