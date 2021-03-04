from leezy import solution, Solution
from leezy.assists import TreeContext, TreeNode


class Q1(Solution):
    @solution
    def threeOrders(self , root ):
        # write code here
        result = [0] * 3
        res1 = self.pre_order(root, [])
        res2 = self.in_order(root, [])
        res3 = self.post_order(root, [])
        result[0], result[1], result[2] = res1, res2, res3
        return result
    
    def pre_order(self, root, res):
        if not root: return
        res.append(root.val)
        self.pre_order(root.left, res)
        self.pre_order(root.right, res)
        return res
    
    def in_order(self, root, res):
        if not root: return
        self.in_order(root.left, res)
        res.append(root.val)
        self.in_order(root.right, res)
        return res
    
    def post_order(self, root, res):
        if not root: return
        self.post_order(root.left, res)
        self.post_order(root.right, res)
        res.append(root.val)
        return res


def main():
    q = Q1()
    q.set_context(TreeContext)
    q.add_case(q.case([1, None, 2, 3]))
    q.run()


if __name__ == '__main__':
    main()
