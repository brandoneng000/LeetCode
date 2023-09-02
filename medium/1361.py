from typing import List
import collections

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        root = 0
        children_nodes = set(leftChild + rightChild)

        for i in range(n):
            if i not in children_nodes:
                root = i
        
        visited = set()
        q = collections.deque([root])

        while q:
            node = q.popleft()

            if node in visited:
                return False
            
            visited.add(node)

            if leftChild[node] != -1:
                q.append(leftChild[node])
            if rightChild[node] != -1:
                q.append(rightChild[node])
        
        return len(visited) == n

        
def main():
    sol = Solution()
    print(sol.validateBinaryTreeNodes(n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]))
    print(sol.validateBinaryTreeNodes(n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]))
    print(sol.validateBinaryTreeNodes(n = 2, leftChild = [1,0], rightChild = [-1,-1]))

if __name__ == '__main__':
    main()