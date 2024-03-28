class Bitset:

    def __init__(self, size: int):
        self.n = size
        self.total = 0
        self.bits = [0] * size
        self.flipped = False

    def fix(self, idx: int) -> None:
        if self.flipped:
            if self.bits[idx] == 1:
                self.total += 1
            self.bits[idx] = 0
        else:
            if self.bits[idx] == 0:
                self.total += 1
            self.bits[idx] = 1

    def unfix(self, idx: int) -> None:
        if self.flipped:
            if self.bits[idx] == 0:
                self.total -= 1
            self.bits[idx] = 1
        else:
            if self.bits[idx] == 1:
                self.total -= 1
            self.bits[idx] = 0

    def flip(self) -> None:
        self.flipped = not self.flipped
        self.total = self.n - self.total

    def all(self) -> bool:
        return self.total == self.n

    def one(self) -> bool:
        return self.total > 0

    def count(self) -> int:
        return self.total

    def toString(self) -> str:
        if self.flipped:
            return ''.join(str(0 if bit else 1) for bit in self.bits)
        else:
            return ''.join(str(bit) for bit in self.bits)


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()