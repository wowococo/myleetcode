from leezy import solution, Solution
from leezy.assists import LinkedListContext


class Q160(Solution):
    @solution
    def getIntersectionNode(self, headA, headB):
        """
        让p ,q 两个指针走相同的距离，p先走A链表，再走B链表；q先走B链表，再走A链表；
        假设两个链表的长度分别是a和b,那么如果两个链表相交，两个指针要走a+b远的路，
        那么p和q最后一段必定是一起的
        """
        p, q = headA, headB
        while p != q:
            p = p.next if p else headB
            q = q.next if q else headA
        return p

def main():
    q = Q160()
    q.set_context(LinkedListContext)
    q.add_case(q.case(8, [4, 1, 8, 4, 5], [5, 6, 1, 8, 4, 5], 2, 3))
    q.run()


if __name__ == '__main__':
    main()
