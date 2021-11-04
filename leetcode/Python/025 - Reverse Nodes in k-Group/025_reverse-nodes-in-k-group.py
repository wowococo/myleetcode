from leezy import solution, Solution
from leezy.assists import ListNode, LinkedListContext

class Q025(Solution):
    @solution
    def reverseKGroup(self, head, k):
        # 48ms 87.82%  recommend lc top answer 
        dummy = ListNode(0)
        dummy.next = head
        front = end = dummy
        while end.next:
            for _ in range(k):
                if end:
                    end = end.next
            if end is None:
                break
            start = front.next
            nxt = end.next
            front.next = self.reverse(start, nxt)
            
            front = end = start

        return dummy.next

    def reverse(self, head, tail):
        if not head or not head.next:
            return head
        prev, cur = tail, head
        while cur != tail:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            
        return prev
    

def main():
    q = Q025()
    q.set_context(LinkedListContext)
    q.add_case(q.case([1, 2, 3, 4, 5], 2))
    q.add_case(q.case([1,2,3,4,5,6,7,8], 3))
    q.run()


if __name__ == '__main__':
    main()
