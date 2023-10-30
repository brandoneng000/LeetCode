from typing import List

class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = kingName
        self.alive = { kingName: True }
        self.family = { kingName: [] }

    def birth(self, parentName: str, childName: str) -> None:
        self.family[parentName].append(childName)
        self.family[childName] = []
        self.alive[childName] = True

    def death(self, name: str) -> None:
        self.alive[name] = False

    def getInheritanceOrder(self) -> List[str]:
        def dfs(name: str):
            if self.alive[name]:
                res.append(name)
            
            for child in self.family[name]:
                dfs(child)
        
        res = []
        dfs(self.king)
        return res
        
# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()