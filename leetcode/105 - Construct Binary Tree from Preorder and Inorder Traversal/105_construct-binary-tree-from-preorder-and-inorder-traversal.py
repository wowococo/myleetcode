from leezy import solution, Solution
from leezy.assists import TreeContext, TreeNode

class Q105(Solution):
    @solution
    def buildTree(self, preorder, inorder):
        if not preorder: return 
        root = TreeNode(preorder[0])
        p = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:p+1], inorder[:p])
        root.right = self.buildTree(preorder[p+1:], inorder[p+1:])
        return root

    from collections import deque


def main():
    q = Q105()
    q.add_case(q.case([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]))
    q.run()


if __name__ == '__main__':
    main()
