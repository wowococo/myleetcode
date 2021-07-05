from leezy import solution, Solution
from leezy.assists import TreeContext


class Q226(Solution):
    @solution
    def invertTree(self, root):
        # 36ms 85.64%
        if not root: return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

def main():
    q = Q226()
    q.set_context(TreeContext)
    q.add_case(q.case([4, 2, 7, 1, 3, 6, 9]))
    q.run()


if __name__ == '__main__':
    main()
