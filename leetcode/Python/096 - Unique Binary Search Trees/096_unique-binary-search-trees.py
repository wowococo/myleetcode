from leezy import solution, Solution


class Q096(Solution):
    @solution
    def numTrees(self, n):
        # catalan 卡特兰数, 题意是节点值 x 从 1 到 n
        # G(n) 表示 n 个节点存在二叉排序树的个数， f(i) 表示以 x 节点值为 root 的二叉排序树的个数
        # G(n) = f(1) + f(2) + f(3) + ... + f(n)
        # 当以 x 为 root 时，左子树节点数为 x-1， 右子树节点数为 n-x
        # f(x) = G(x-1) * G(n-x)
        # 即 G(n) = G(0)*G(n-1) + G(1)*G(n-2) + G(2)*G(n-3) + ... + G(n-1)*G(0);   G(0) = G(1) = 1
        # 将卡特兰公式转化为动态规划, dp[i] 表示 G(n), x 用 j 代
        # 28ms, 88.11%
        dp = [0] * (n+1)
        dp[0] = dp[1] = 1     
        for i in range(2, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1] * dp[i-j]
        
        return dp[n]

def main():
    q = Q096()
    q.add_case(q.case(3).assert_equal(5))
    q.add_case(q.case(1).assert_equal(1))
    q.add_case(q.case(2).assert_equal(2))
    q.run()


if __name__ == '__main__':
    main()
