from leezy import solution, Solution
from leezy.assists import LinkedListContext, ListNode


class Q206(Solution):
    @solution
    def reverseList(self, head):
        dummy = ListNode()
        while head:
           nxt = head.next
           head.next = dummy.next
           dummy.next = head
           head = nxt
        return dummy.next

    @solution
    def reverse_rec(self, head):
        if head is None or head.next is None:
            return head
        cur = self.reverse_rec(head.next)
        head.next.next = head
        head.next = None
        return cur        

    @solution
    def reverse_rec_popular(self, head):
        if not head:
            return
        def rec(node):
            if node.next is None:
                return node, node
            head, tail = rec(node.next)
            node.next = None
            tail.next = node
            tail = tail.next
            return head, tail
        rev, _ = rec(head)
        return rev
               

def main():
    q = Q206()
    q.set_context(LinkedListContext)
    make = ListNode.make_linked_list
    # q.add_case(q.case([1, 2, 3, 4, 5]).assert_equal(make([5, 4, 3, 2, 1])))
    q.add_case(q.case([1, 2, 3, 4, 5]))
    q.run()


if __name__ == '__main__':
    main()
