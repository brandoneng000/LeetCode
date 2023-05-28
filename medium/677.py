import collections
class MapSum:

    def __init__(self):
        self.letters = {}
        self.val = 0

    def insert(self, key: str, val: int) -> None:
        temp = self
        for letter in key:
            if letter not in temp.letters:
                temp.letters[letter] = MapSum()
            temp = temp.letters[letter]
        temp.val = val

    def sum(self, prefix: str) -> int:
        temp = self
        total = 0
        for letter in prefix:
            if letter in temp.letters:
                temp = temp.letters[letter]
            else:
                return total
        
        q = collections.deque([temp.letters[letter] for letter in temp.letters])
        total += temp.val
        while q:
            node = q.popleft()
            total += node.val
            q.extend([node.letters[letter] for letter in node.letters])

        return total
            


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)