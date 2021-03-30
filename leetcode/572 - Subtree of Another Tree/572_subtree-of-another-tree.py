from leezy import solution, Solution
from leezy.assists import TreeContext

class Q572(Solution):
    @solution
    def isSubtree(self, s, t):
        if s is None and t is None:
            return True
        if not s or not t:
            return False
        return self.isSametree(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    
    def isSametree(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        return s.val == t.val and self.isSametree(s.left, t.left) and self.isSametree(s.right, t.right)


def main():
    q = Q572()
    q.set_context(TreeContext)
    q.add_case(q.case([3, 4, 5, 1, 2], [4, 1, 2]).assert_equal(True))
    q.add_case(q.case([3,4,5,1,2,None,None,None,None,0], [4,1,2]).assert_equal(False))
    q.run()


if __name__ == '__main__':
    main()
