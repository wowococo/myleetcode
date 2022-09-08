from leezy import solution, Solution
from leezy.assists import TreeContext
from collections import deque


class Q958(Solution):
    @solution
    def isCompleteTree(self, root):
        # 验证是否是完全二叉树，层次遍历（联想到deque）对每个节点编号，如果发现相邻节点值超过 1，则不是完全二叉树。
        if root is None: return True   # 树的题，都要先判断一下这句
        d = deque()
        d.append((root, 1))
        prev = 0
        while d:
            n = len(d)
            for _ in range(n):
                node, x = d.popleft()
                if x - prev > 1:
                    return False
                prev = x
                if node.left:
                    d.append((node.left, 2*x))
                if node.right:
                    d.append((node.right, 2*x+1))
        return True
    
def main():
    q = Q958()
    q.set_context(TreeContext)
    q.add_case(q.case([1, 2, 3, 4, 5, 6]))
    q.add_case(q.case([]))
    q.run()


if __name__ == '__main__':
    main()
