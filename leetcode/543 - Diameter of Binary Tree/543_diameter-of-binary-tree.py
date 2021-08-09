from leezy import solution, Solution
from leezy.assists import TreeContext


class Q543(Solution):
    @solution
    def diameterOfBinaryTree(self, root):
        # 32ms 99.28%, 16.7M 86.73%
        self.max = 0

        self.depth(root)

        return self.max
        
    def depth(self, root):
        if root is None:
            return 0
        l = self.depth(root.left)
        r = self.depth(root.right)
        
        self.max = max(l + r, self.max)

        return max(l, r) + 1

def main():
    q = Q543()
    q.set_context(TreeContext)
    q.add_case(q.case([1, 2, 3, 4, 5]))
    q.run()


if __name__ == '__main__':
    main()
