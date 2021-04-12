from leezy import solution, Solution
from leezy.assists import LinkedListContext


class Q328(Solution):
    @solution
    def oddEvenList(self, head):
        if not head or not head.next:
            return head
        evenhead = head.next
        odd, even = head, evenhead 
        while even and even.next:
            # 先奇后偶，和最后链表一样
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenhead
        return head

    @solution
    def oddEvenList(self, head):
        # 暴力解法，我自己都写不出第二遍
        if not head or not head.next:
            return head
        if not head.next.next:
            return head
        c = 1
        odd = tail = head
        even = head.next
        while tail:
            tail = tail.next
            c += 1
            if c % 2 == 1 and tail:
                tmp = tail.next
                tail.next = odd.next
                even.next = tmp
                odd.next = tail
                tail = even 
                even = even.next
                odd = odd.next
        return head


def main():
    q = Q328()
    q.set_context(LinkedListContext)
    q.add_case(q.case([1, 2, 3, 4, 5]))
    q.add_case(q.case([2, 1, 3, 5, 6, 4, 7]))
    q.add_case(q.case([1]))
    q.run()


if __name__ == '__main__':
    main()
