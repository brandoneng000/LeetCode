import collections

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        tree = []
        queue = collections.deque([root])
        while queue:
            val = queue.popleft()
            if not val:
                tree.append(None)
            else:
                tree.append(str(val.val))
                queue.append(val.left)
                queue.append(val.right)
        
        return ' '.join(tree)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = collections.deque(data.split(' '))
        nodes = collections.deque([])
        left = right = True
        root = None
        parents = collections.deque([])
        
        while data:
            val = data.popleft()
            if val != 'n':
                node = TreeNode(int(val))
            else:
                node = None
            nodes.append(node)
        
        for node in nodes:
            if not root:
                root = node
            if node:
                parents.append(node)
            if not left:
                parent.left = node
                left = True
            elif not right:
                parent.right = node
                right = True
            
            if left and right and parents:
                parent = parents.popleft()
                left = False
                right = False

        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

def main():
    test1()

def test1():
    codec = Codec()
    print(codec.deserialize("1 2 3 n n 4 5 n n n n"))

if __name__ == '__main__':
    main()