from leezy import solution, Solution
from leezy.assists import TreeContext, TreeNode


class Q113(Solution):
    @solution
    def pathSum(self, root, targetSum):
        if root is None: return []
        cur, total = [], []
        self.dfs(root, targetSum, cur, total)
        return total
        
    def dfs(self, node, target, cur, total):
        if not node.left and not node.right:
            if node.val == target:
                total.append(cur+[node.val])
            return
        
        cur.append(node.val)
        if node.left:
            self.dfs(node.left, target-node.val, cur, total)
        if node.right:
            self.dfs(node.right, target-node.val, cur, total)
        cur.pop()



def main():
    q = Q113()
    q.set_context(TreeContext)
    q.add_case(q.case([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1], 22))
    q.run()


if __name__ == '__main__':
    main()
