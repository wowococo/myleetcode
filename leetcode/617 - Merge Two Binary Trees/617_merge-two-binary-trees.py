from leezy import solution, Solution
from leezy.assists import TreeContext, TreeNode

class Q617(Solution):
    @solution
    def mergeTrees(self, root1, root2):
        # 合并两个二叉树, 两棵树的每个对应结点都是要判断这三种情况,因此考虑使用递归
        if root1 is None and root2 is None:
            return 
        if root1 and root2:
            tree = TreeNode(root1.val+root2.val)
            tree.left = self.mergeTrees(root1.left, root2.left)
            tree.right = self.mergeTrees(root1.right, root2.right)
        else:
            if root1: tree = root1
            if root2: tree = root2
        
        return tree


def main():
    q = Q617()
    q.set_context(TreeContext)
    q.add_case(q.case([1, 3, 2, 5], [2, 1, 3, None, 4, None, 7]))
    q.run()


if __name__ == '__main__':
    main()
