class Node:
    def __init__(self, val = 0, next = None) -> None:
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.head = None

    def get(self, index: int) -> int:
        if self.size <= index:
            return -1
        
        temp = self.head
        while index > 0:
            index -= 1
            temp = temp.next
        return temp.val


    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        self.head = node
        self.size += 1
        

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        if self.size == 0:
            self.head = node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node
        self.size += 1
        
    def addAtIndex(self, index: int, val: int) -> None:
        if self.size < index:
            return
        
        if index == 0:
            self.addAtHead(val)
        else:
            self.size += 1
            temp = self.head
            for i in range(index - 1):
                temp = temp.next
            node = Node(val, temp.next)
            temp.next = node

    def deleteAtIndex(self, index: int) -> None:
        if self.size <= index:
            return
        
        if index == 0:
            self.head = self.head.next
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            temp.next = temp.next.next
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)