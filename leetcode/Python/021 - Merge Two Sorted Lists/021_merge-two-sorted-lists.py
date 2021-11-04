from leezy import solution, Solution
from leezy.assists import ListNode, LinkedListContext

class Q021(Solution):
    @solution
    def mergeTwoLists(self, l1, l2):
        dummy = l = ListNode()
        while l1 and l2:
            if l1.val >= l2.val:
                l.next = l2
                l2 = l2.next
            else:
                l.next = l1
                l1 = l1.next
            l = l.next
        if l1: l.next = l1
        if l2: l.next = l2
        return dummy.next

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = tail = ListNode(0)
        while l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            tail.next = l1
            l1 = l1.next
            tail = tail.next
        if l1: tail.next = l1
        if l2: tail.next = l2
        return dummy.next

def main():
    q = Q021()
    q.set_context(LinkedListContext)
    q.add_case(q.case([1, 2, 4], [1, 3, 4]))
    q.run()


if __name__ == '__main__':
    main()
