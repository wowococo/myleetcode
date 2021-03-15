from leezy import solution, Solution
from leezy.assists import TreeContext

class Q101(Solution):
    @solution
    def isSymmetric(self, root):
        if root is None:
            return True
        return self.scan(root.left, root.right)

    def scan(self, p, q):
        if p is None and q is None:
            return True
        elif p and q and p.val == q.val:
            return self.scan(p.left, q.right) and self.scan(p.right, q.left)
        else:
            return False
        

def main():
    q = Q101()
    q.set_context(TreeContext)
    q.add_case(q.case([1, 2, 2, 3, 4, 4, 3]))
    q.add_case(q.case([1,2,2,None, 3, None, 3]))
    q.run()


if __name__ == '__main__':
    main()
