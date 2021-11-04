from leezy import solution, Solution
from leezy.assists import TreeContext, TreeNode

class Q110(Solution):
    @solution
    def isBalanced(self, root):
        # 自底向上, 遇到不满足情况直接返回（剪枝）
        return self.recur(root) != -1

    def recur(self, root):
        if not root: return 0
        left = self.recur(root.left)
        if left == -1: return -1
        right = self.recur(root.right)
        if right == -1: return -1
        return max(left, right) + 1 if abs(left-right) < 2 else -1



def main():
    q = Q110()
    q.set_context(TreeContext)
    q.add_case(q.case([3, 9, 20, None, None, 15, 7]))
    q.add_case(q.case([]))
    q.add_case(q.case([3, 9, 20, None, None, 15, 7, 2]))
    q.run()


if __name__ == '__main__':
    main()
