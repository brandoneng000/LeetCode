from typing import Optional, List
from collections import deque

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        q = deque([(head, root)])

        while q:
            linked_list_node, tree_node = q.popleft()

            if linked_list_node.val == tree_node.val:
                if not linked_list_node.next:
                    return True
                
                if tree_node.left:
                    q.append((linked_list_node.next, tree_node.left))
                
                if tree_node.right:
                    q.append((linked_list_node.next, tree_node.right))
            
            if linked_list_node != head:
                continue
            
            if tree_node.left:
                q.append((head, tree_node.left))
            
            if tree_node.right:
                q.append((head, tree_node.right))
        
        return False

    # def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
    #     def dfs(head: ListNode, root: TreeNode):
    #         if not head:
    #             return True
    #         if not root:
    #             return False
            
    #         return root.val == head.val and (dfs(head.next, root.left) or dfs(head.next, root.right))
        
    #     if not head:
    #         return True
    #     if not root:
    #         return False
        
    #     return dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

        