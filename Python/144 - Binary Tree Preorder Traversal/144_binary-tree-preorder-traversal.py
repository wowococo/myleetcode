from leezy import solution, Solution
from leezy.assists import TreeContext, TreeNode


class Q144(Solution):
    @solution
    def preorderTraversal(self, root):
        def preorder(root, res):
            if not root: return
            res.append(root.val)    
            if root.left: preorder(root.left, res)
            if root.right: preorder(root.right, res)
        
        res = []
        preorder(root, res)
        return res


def main():
    q = Q144()
    q.set_context(TreeContext)
    q.add_case(q.case([1, None, 2, 3]))
    q.run()


if __name__ == '__main__':
    main()
