from typing import List
from collections import defaultdict, deque

class LockingTree:

    def __init__(self, parent: List[int]):
        self.children = defaultdict(list)
        self.parents = {}
        self.locks = [-1] * len(parent)

        for i, node in enumerate(parent):
            self.children[node].append(i)
            self.parents[i] = node

    def lock(self, num: int, user: int) -> bool:
        if self.locks[num] == -1:
            self.locks[num] = user
            return True
        
        return False

    def unlock(self, num: int, user: int) -> bool:
        if self.locks[num] == user:
            self.locks[num] = -1
            return True
        
        return False
        
    def upgrade(self, num: int, user: int) -> bool:
        node = num

        while node != -1:
            if self.locks[node] != -1:
                return False
            node = self.parents[node]
        
        q = deque([num])
        locked_desc = False
        desc = []

        while q:
            node = q.popleft()

            locked_desc = locked_desc or (self.locks[node] != -1)

            for child in self.children[node]:
                desc.append(child)
                q.append(child)
        
        if locked_desc:
            self.locks[num] = user
            for c in desc:
                self.locks[c] = -1
            return True
        
        return False



        


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)