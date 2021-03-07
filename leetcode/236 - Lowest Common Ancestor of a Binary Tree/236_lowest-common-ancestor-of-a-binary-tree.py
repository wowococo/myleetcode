from leezy import solution, Solution
from leezy.assists import TreeContext

class Q236(Solution):

    def __init__(self):
        self.ans = None

    @solution
    def lowestCommonAncestor(self, root, p, q):
        def recur_tree(current):
            if not current: return False
            m = current.val == p or current.val == q
            left = recur_tree(current.left)
            right = recur_tree(current.right)
            if m + left + right >= 2:
                self.ans = current
            return m or left or right
        recur_tree(root)
        return self.ans
    
def main():
    q = Q236()
    q.set_context(TreeContext)
    q.add_case(q.case([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 1))
    q.run()


if __name__ == '__main__':
    main()
