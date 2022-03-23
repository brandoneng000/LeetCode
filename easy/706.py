class ListNode:
     def __init__(self, key=0, val=0, next=None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):
        self.head = ListNode(-1, -1)

    def put(self, key: int, value: int) -> None:
        temp = self.head
        while temp:
            if temp.key == key:
                temp.val = value
                return
            if temp.next:
                temp = temp.next
            else:
                break
        if not temp.next:
            temp.next = ListNode(key, value)

    def get(self, key: int) -> int:
        temp = self.head
        while temp:
            if temp.key == key:
                return temp.val
            temp = temp.next
        return -1

    def remove(self, key: int) -> None:
        cur = self.head.next
        prev = self.head

        while cur:
            if cur.key == key:
                prev.next = cur.next
                break
            else:
                prev = cur
                cur = cur.next

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)