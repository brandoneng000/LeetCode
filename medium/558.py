# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        if quadTree1.isLeaf:
            return quadTree1 if quadTree1.val else quadTree2
        elif quadTree2.isLeaf:
            return quadTree2 if quadTree2.val else quadTree1
        else:
            t_left = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
            t_right = self.intersect(quadTree1.topRight, quadTree2.topRight)
            b_left = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
            b_right = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)
            if t_left.isLeaf and t_right.isLeaf and b_left.isLeaf and b_right.isLeaf \
                and t_left.val == t_right.val == b_left.val == b_right.val:
                node = Node(t_left.val, True, None, None, None, None)
            else:
                node = Node(False, False, t_left, t_right, b_left, b_right)

        return node
