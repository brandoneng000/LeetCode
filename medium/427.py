from typing import List
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
    def construct(self, grid: List[List[int]]) -> 'Node':
        def check_grid(x, y, end) -> bool:
            check = grid[x][y]

            for i in range(x, x + end):
                for j in range(y, y + end):
                    if check != grid[i][j]:
                        return False
                    
            return True
        
        def generate_node(x, y, end):
            if check_grid(x, y, end):
                return Node(grid[x][y], True)
            
            root = Node(0, False)
            side = end // 2
            root.topLeft = generate_node(x, y, side)
            root.topRight = generate_node(x, y + side, side)
            root.bottomLeft = generate_node(x + side, y, side)
            root.bottomRight = generate_node(x + side, y + side, side)

            return root
        
        return generate_node(0, 0, len(grid))


    
