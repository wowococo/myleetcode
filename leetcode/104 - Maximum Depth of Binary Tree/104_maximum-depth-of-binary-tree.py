from leezy import solution, Solution
from leezy.assists import TreeContext, TreeNode
from collections import deque


class Q104(Solution):
    @solution
    def maxDepth(self, root):
        # 这题的最大深度感觉跟层数一样, root那里是 1
        # BFS
        if not root: return 0
        d = deque([root])
        depth = 0
        while d:
            n = len(d)
            depth += 1
            for _ in range(n):
                node = d.popleft()
                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)
        return depth

    @solution
    def maxDepth(self, root):
        # DFS
        if not root: return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1

def main():
    q = Q104()
    q.set_context(TreeContext)
    q.add_case(q.case([3, 9, 20, None, None, 15, 7]))
    q.run()


if __name__ == '__main__':
    main()
