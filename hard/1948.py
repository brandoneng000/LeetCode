from typing import List
from collections import defaultdict

class Node:
    def __init__(self, name: str):
        self.name = name
        self.children = {}
        self.signature = ""

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        def dfs(node: Node):
            if not node.children:
                node.signature = ""
                return ""
            
            child_signatures=  []

            for name, child in sorted(node.children.items()):
                child_signature = dfs(child)
                child_signatures.append(f"{name}({child_signature})")
            
            node.signature = "".join(child_signatures)
            signature_count[node.signature] += 1
            
            return node.signature
        
        def dfs2(node: Node):
            if node.children and signature_count[node.signature] >= 2:
                return
            current_path.append(node.name)
            res.append(current_path.copy())

            for name, child in sorted(node.children.items()):
                dfs2(child)

            current_path.pop()

        root = Node("")

        for path in paths:
            node = root

            for folder in path:
                if folder not in node.children:
                    node.children[folder] = Node(folder)
                node = node.children[folder]
        
        signature_count = defaultdict(int)
        res = []
        current_path = []
        dfs(root)

        for name, child in sorted(root.children.items()):
            dfs2(child)
        
        return res

        
def main():
    sol = Solution()
    print(sol.deleteDuplicateFolder([["a"],["c"],["d"],["a","b"],["c","b"],["d","a"]]))
    print(sol.deleteDuplicateFolder([["a"],["c"],["a","b"],["c","b"],["a","b","x"],["a","b","x","y"],["w"],["w","y"]]))
    print(sol.deleteDuplicateFolder([["a","b"],["c","d"],["c"],["a"]]))

if __name__ == '__main__':
    main()