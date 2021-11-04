from leezy import solution, Solution
from leezy.assists import TreeContext, TreeNode
from collections import deque

class Q103(Solution):
    @solution
    def zigzagLevelOrder(self, root):
        if not root: return []
        res = []
        d = deque([root])
        ltr = True
        while d:
            n = len(d)
            level = [0] * n
            for i in range(n):
                node = d.popleft()
                if ltr:
                    level[i] = node.val
                else:
                    level[n-i-1] = node.val
                if node.left: d.append(node.left)
                if node.right: d.append(node.right)
            res.append(level)
            ltr = not ltr
        return res
            

def main():
    q = Q103()
    q.set_context(TreeContext)
    q.add_case(q.case([3, 9, 20, None, None, 15, 7]))
    q.run()


if __name__ == '__main__':
    main()
