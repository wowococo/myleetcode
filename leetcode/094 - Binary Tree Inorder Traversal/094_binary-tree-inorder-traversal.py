from leezy import solution, Solution
from leezy.assists import TreeContext, TreeNode

class Q094(Solution):
    @solution
    def inorderTraversal(self, root):
        def in_order(root, res):
            if not root: return
            in_order(root.left, res)
            res.append(root.val)
            in_order(root.right, res)

        res = []
        in_order(root, res)
        return res

def main():
    q = Q094()
    q.set_context(TreeContext)
    q.add_case(q.case([1, None, 2, 3]).assert_equal([1, 3, 2]))
    q.run()


if __name__ == '__main__':
    main()
