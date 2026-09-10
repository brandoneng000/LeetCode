from typing import List

class SQL:

    def __init__(self, names: List[str], columns: List[int]):
        self.rows = { name: {} for name in names }
        self.cols = { name: col for name, col in zip(names, columns) }
        self.id = { name: 1 for name in names }

    def ins(self, name: str, row: List[str]) -> bool:
        if name not in self.cols or len(row) != self.cols[name]:
            return False

        self.rows[name][self.id[name]] = row
        self.id[name] += 1

        return True
        
    def rmv(self, name: str, rowId: int) -> None:
        if name in self.rows and rowId in self.rows[name]:
            self.rows[name].pop(rowId)
        

    def sel(self, name: str, rowId: int, columnId: int) -> str:
        columnId -= 1

        if name in self.rows:
            if rowId in self.rows[name]:
                if columnId < self.cols[name]:
                    return self.rows[name][rowId][columnId]

        return "<null>"

    def exp(self, name: str) -> List[str]:
        if name not in self.rows:
            return ","

        res = []

        for r in self.rows[name]:
            res.append(','.join([str(r)] + self.rows[name][r]))

        return res


# Your SQL object will be instantiated and called as such:
# obj = SQL(names, columns)
# param_1 = obj.ins(name,row)
# obj.rmv(name,rowId)
# param_3 = obj.sel(name,rowId,columnId)
# param_4 = obj.exp(name)