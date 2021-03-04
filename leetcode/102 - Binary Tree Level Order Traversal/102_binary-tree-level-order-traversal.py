import queue
from leezy import solution, Solution
from leezy.assists import TreeContext, TreeNode

class Q102(Solution):
    @solution
    def levelOrder(self, root):
        # import pdb; pdb.set_trace()
        if not root: return
        res = []
        q = queue.Queue()
        q.put(root)
        while q.qsize():
            node = q.get()
            res.append(node.val)
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)
        return res

        

def main():
    q = Q102()
    q.set_context(TreeContext)
    q.add_case(q.case([3, 9, 20, None, None, 15, 7]))
    q.run()


if __name__ == '__main__':
    main()
