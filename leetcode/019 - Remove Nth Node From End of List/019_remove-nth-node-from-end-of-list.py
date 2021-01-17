from leezy import solution, Solution
from leezy.assists import ListNode

class Q019(Solution):
    @solution
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        first = second = dummy
        for i in range(n+1):
            first = first.next
        while first:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next

    @solution
    def removeNthFromEnd2(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        first, l = head, 0
        while first:
            l += 1 
            first = first.next
        first = dummy
        l -= n
        for i in range(l):   
            # 不用判断first 题目保证了要删除的结点是有效的
            first = first.next   
        # while l > 0:  # 这三步和上面的for循环效果一样     
        #     first = first.next    
        #     l -= 1
        first.next = first.next.next
        return dummy.next
            

def main():
    q = Q019()
    q.add_case(q.case([1, 2, 3, 4, 5], 2))
    q.run()


if __name__ == '__main__':
    main()
