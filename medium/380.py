import random

class RandomizedSet:
    def __init__(self):
        self.random_list = []
        self.random_dict = {}
        
    def insert(self, val: int) -> bool:
        if val not in self.random_dict:
            self.random_list.append(val)
            self.random_dict[val] = len(self.random_list) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.random_dict:
            index, last_val = self.random_dict[val], self.random_list[-1]
            self.random_list[index] = last_val
            self.random_dict[last_val] = index
            self.random_list.pop()
            self.random_dict.pop(val)
            return True
        return False
        
    def getRandom(self) -> int:
        return random.choice(self.random_list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()