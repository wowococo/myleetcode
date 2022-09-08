from leezy import solution, Solution
from leezy.assists import TreeContext, TreeNode


class Q145(Solution):
    @solution
    def postorderTraversal(self, root):
        def postorder(root, res):
            if not root: return
            postorder(root.left, res)
            postorder(root.right, res)
            res.append(root.val)

        res = []
        postorder(root, res)
        return res

def main():
    q = Q145()
    q.set_context(TreeContext)
    q.add_case(q.case([1, None, 2, 3]))
    q.run()


if __name__ == '__main__':
    main()
