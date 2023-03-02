from typing import Optional, List
import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        binary_tree_dict = collections.defaultdict(list)

        def traverse(root: TreeNode, level: int, binary_tree_dict: dict):
            if not root:
                return
            
            binary_tree_dict[level].append(root.val)
            traverse(root.left, level + 1, binary_tree_dict)
            traverse(root.right, level + 1, binary_tree_dict)
        
        traverse(root, 1, binary_tree_dict)

        return (sum(binary_tree_dict[vals]) / len(binary_tree_dict[vals]) for vals in binary_tree_dict)