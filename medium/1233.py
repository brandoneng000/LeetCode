from typing import List
import collections

class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.end = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
    
    def add_node(self, child: List[str]):
        temp = self.root
        for f in child:
            if f not in temp.children:
                temp.children[f] = TrieNode()
            temp = temp.children[f]
            if temp.end:
                return False
            
        temp.end = True
        return True

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder_size = Trie()
        res = []
        for f in sorted(folder, key=lambda x: x.count('/')):
            if folder_size.add_node(f.split('/')):
                res.append(f)
        
        return res

        
def main():
    sol = Solution()
    print(sol.removeSubfolders(["/ah/al/am","/ah/al"]))
    print(sol.removeSubfolders(["/a","/a/b","/c/d","/c/d/e","/c/f"]))
    print(sol.removeSubfolders(["/a","/a/b/c","/a/b/d"]))
    print(sol.removeSubfolders(["/a/b/c","/a/b/ca","/a/b/d"]))

if __name__ == '__main__':
    main()