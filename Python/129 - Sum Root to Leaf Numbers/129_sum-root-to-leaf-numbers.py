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
    
    @solution
    def sumNumbers_better(self, root):
        if root is None: return 0
        self.ans = 0
        self.collect(root, 0)
        return self.ans
    
    def collect(self, node, val):
        if not node.left and not node.right:
            self.ans += val * 10 + node.val
            return
        val  = val * 10 + node.val
        if node.left:
            self.collect(node.left, val)
        if node.right:
            self.collect(node.right, val)
        


        

def main():
    q = Q129()
    q.set_context(TreeContext)
    q.add_case(q.case([1, 2, 3]))
    q.add_case(q.case([0, 1]))
    q.run()


if __name__ == '__main__':
    main()
