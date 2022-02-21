# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # if not head:
        #     return None

        # newHead = head
        # if head.next:
        #     newHead = self.reverseList(head.next)
        #     head.next.next = head
        # head.next = None
        # return newHead

        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

        # if not head:
        #     return
        # tail = ListNode()
        # first = True
        # while(True):
        #     temp = ListNode(head.val, tail)
        #     tail = temp
            
        #     if first:
        #         temp.next = None
        #         first = False

        #     if not head.next:
        #         break
        #     else:
        #         head = head.next
        
        # while(tail.next):
        #     if not tail.next.next:
        #         tail.next = None
        #     else:
        #         tail = tail.next

        return temp

def main():
    sol = Solution()
    head_one = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
    print(sol.reverseList(head_one).val)


if __name__ == '__main__':
    main()