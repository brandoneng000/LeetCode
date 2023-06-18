from typing import List
import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        # self.prev = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = collections.defaultdict(list)
        def build_graph(root: TreeNode, prev: TreeNode):
            if root and prev:
                graph[root.val].append(prev.val)
                graph[prev.val].append(root.val)
            if root.left:
                build_graph(root.left, root)
            if root.right:
                build_graph(root.right, root)
        
        build_graph(root, None)
        visited = set([target.val])
        res = []

        q = collections.deque([(target.val, 0)])
        while q:
            node, dist = q.popleft()

            if dist == k:
                res.append(node)
                continue

            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append((neighbor, dist + 1))
        
        return res

    # def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
    #     def add_prev(root: TreeNode, prev: TreeNode):
    #         if root:
    #             root.prev = prev
    #             add_prev(root.left, root)
    #             add_prev(root.right, root)

    #     add_prev(root, None)
    #     res = []
    #     visited = set()
    #     def dfs(root: TreeNode, dist: int):
    #         if not root or root in visited:
    #             return
            
    #         visited.add(root)
    #         if dist == 0:
    #             res.append(root.val)
    #             return
            
    #         dfs(root.prev, dist - 1)
    #         dfs(root.left, dist - 1)
    #         dfs(root.right, dist - 1)
        
    #     dfs(target, k)
    #     return res