class Fancy:
    def __init__(self):
        self.MOD = 1_000_000_007
        self.nums = []
        self.a = 1
        self.b = 0

    def append(self, val: int) -> None:
        x = (val - self.b + self.MOD) % self.MOD
        self.nums.append(x * pow(self.a, self.MOD - 2, self.MOD) % self.MOD)    

    def addAll(self, inc: int) -> None:
        self.b = (self.b + inc) % self.MOD

    def multAll(self, m: int) -> None:
        self.a = (self.a * m) % self.MOD
        self.b = (self.b * m) % self.MOD


    def getIndex(self, idx: int) -> int:
        if idx >= len(self.nums):
            return -1

        return (self.a * self.nums[idx] + self.b) % self.MOD


def main():
    fancy = Fancy()
    fancy.append(2)  
    fancy.addAll(3)  
    fancy.append(7)   
    fancy.multAll(2)
    print(fancy.getIndex(0))    
    fancy.addAll(3) 
    fancy.append(10) 
    fancy.multAll(2)
    print(fancy.getIndex(0))
    print(fancy.getIndex(1))
    print(fancy.getIndex(2))

if __name__ == '__main__':
    main()

# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)