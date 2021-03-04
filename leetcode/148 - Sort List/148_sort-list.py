from leezy import solution, Solution
from leezy.assists import LinkedListContext, ListNode


class Q148(Solution):
    @solution
    def sortList(self, head):
        if not head or not head.next: return head
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        mid = slow.next
        slow.next = None
        return self.merge(self.sortList(head), self.sortList(mid))

    def merge(self, l1, l2):
        dummy = tail = ListNode(0)
        while l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            tail.next = l1
            tail = tail.next
            l1 = l1.next
        if l1: tail.next = l1
        if l2: tail.next = l2
        return dummy.next


def main():
    q = Q148()
    q.set_context(LinkedListContext)
    q.add_case(q.case([4, 2, 1, 3]))
    q.run()


if __name__ == '__main__':
    main()
