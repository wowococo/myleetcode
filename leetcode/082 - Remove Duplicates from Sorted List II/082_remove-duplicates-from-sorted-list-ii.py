from leezy import solution, Solution
from leezy.assists import ListNode, LinkedListContext


class Q082(Solution):
    @solution
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head
        dummy = ListNode(None)
        dummy.next = head
        prev = dummy
        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur = cur.next
            if prev.next == cur:
                prev = prev.next
            else:
                prev.next = cur.next
            cur = cur.next
        return dummy.next


def main():
    q = Q082()
    q.set_context(LinkedListContext)
    q.add_case(q.case([1, 2, 3, 3, 4, 4, 5]))
    q.add_case(q.case([1, 1, 1, 2, 5]))
    q.run()


if __name__ == '__main__':
    main()
