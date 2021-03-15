from leezy import solution, Solution
from leezy.assists import TreeContext


class Q129(Solution):
    @solution
    def sumNumbers(self, root):
        if root is None: return 0
        cur = ''
        self.total = 0
        self.dfs(root, cur)
        return self.total

    def dfs(self, node, cur):
        if not node.left and not node.right:
            self.total += int(cur+str(node.val))
            return
        cur += str(node.val)
        if node.left:
            self.dfs(node.left, cur)
        if node.right:
            self.dfs(node.right, cur)
        cur = cur[:-1]
    

def main():
    q = Q129()
    q.set_context(TreeContext)
    q.add_case(q.case([1, 2, 3]))
    q.add_case(q.case([0, 1]))
    q.run()


if __name__ == '__main__':
    main()
