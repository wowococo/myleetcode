from leezy import solution, Solution
from leezy.assists import TreeContext

class Q337(Solution):
    @solution
    def rob(self, root):
        # TLE 122/124
        ans = self.dfs(root)
        return ans
    
    def dfs(self, node):
        if node is None:
            return 0
        ans = node.val
        if node.left:
            ans += self.dfs(node.left.left) + self.dfs(node.left.right)
        if node.right:
            ans += self.dfs(node.right.left) + self.dfs(node.right.right)
        ans = max(ans, self.dfs(node.left) + self.dfs(node.right))
        return ans

    @solution
    def rob_memo(self, root):
        # 52ms 43.08%
        memo = {}
        def rob_recur(node):
            if node is None:
                return 0
            if node in memo:
                return memo[node]
            # 抢
            rob = node.val
            if node.left:
                rob += rob_recur(node.left.left) + rob_recur(node.left.right)
            if node.right:
                rob += rob_recur(node.right.left) + rob_recur(node.right.right)
            # 不抢
            not_rob = rob_recur(node.left) + rob_recur(node.right)

            memo[node] = max(rob, not_rob)
            
            return memo[node]

        return rob_recur(root)

    @solution
    def rob_tuple(self, root):
        # 返回两个值，这个节点抢和不抢的各自最大收益
        def rob_(node):
            if node is None:
                return 0, 0
            
            l_rob, l_not_rob = rob_(node.left)
            r_rob, r_not_rob = rob_(node.right)
            do = node.val + l_not_rob + r_not_rob
            not_do = max(l_rob, l_not_rob) + max(r_rob, r_not_rob)

            return do, not_do
        
        return max(rob_(root))


def main():
    q = Q337()
    q.set_context(TreeContext)
    q.add_case(q.case([3, 2, 3, None, 3, None, 1]).assert_equal(7))
    q.add_case(q.case([3,4,5,1,3,None,1]).assert_equal(9))
    q.add_case(q.case([4,1,None,2,None,3]).assert_equal(7))
    q.run()


if __name__ == '__main__':
    main()
