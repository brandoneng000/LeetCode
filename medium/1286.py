from typing import List

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        def helper(cur: List[str], index: int):
            if len(cur) == combinationLength:
                self.combos.append("".join(cur))
                return
            
            for i in range(index, len(char_list)):
                cur.append(char_list[i])
                helper(cur, i + 1)
                cur.pop()
        
        char_list = sorted(characters)
        self.combos = []
        self.index = 0
        helper([], 0)
        self.combos.sort()

    def next(self) -> str:
        if self.hasNext():
            res = self.combos[self.index]
            self.index += 1
            return res
        

    def hasNext(self) -> bool:
        return self.index < len(self.combos)


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()