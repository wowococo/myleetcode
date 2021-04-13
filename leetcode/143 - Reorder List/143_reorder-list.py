from leezy import solution, Solution
from leezy.assists import LinkedListContext

class Q143(Solution):
    @solution
    def reorderList(self, head):
        # 92 ms 64.93%
        # 根据链表长度确定递归出口
        # 只需在递归出口定义将“处理完的链表”指向 None, 因为每次递归“处理完的链表”尾结点都是3指向None， 2 -> 4 -> 3 > None
        # 参考 https://leetcode-cn.com/problems/reorder-list/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-34/
        if not head or not head.next:
            return head
        node = head
        n = 0
        while node:
            n += 1
            node = node.next
        def reorder(head, length):
            if length == 1:
                outtail = head.next
                head.next = None   
                return outtail
            if length == 2:
                outtail = head.next.next
                head.next.next = None
                return outtail

            tail = reorder(head.next, length-2)
            outtail = tail.next
            subhead = head.next
            head.next = tail
            tail.next = subhead

            return outtail

        reorder(head, n)
        return head





def main():
    q = Q143()
    q.set_context(LinkedListContext)
    q.add_case(q.case([1, 2, 3, 4]))
    q.add_case(q.case([1,2,3,4,5]))
    q.run()


if __name__ == '__main__':
    main()
