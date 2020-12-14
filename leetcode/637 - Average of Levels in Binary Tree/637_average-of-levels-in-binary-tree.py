from collections import deque
from leezy import solution, Solution


class Q637(Solution):
    @solution
    def averageOfLevels(self, root):
        res = list()
        if not root: return res
        q = deque([root])
        while q:
            n = len(q)
            level = list()
            for _ in range(n):
                node = q.popleft()
                level.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(sum(level) / n)
        return res

def main():
    q = Q637()
    q.add_case(q.case([3, 9, 20, 15, 7]))
    q.run()


if __name__ == '__main__':
    main()
