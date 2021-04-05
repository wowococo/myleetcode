from leezy import solution, Solution


class Q072(Solution):
    @solution
    def minDistance_review(self, word1, word2):
#      1. 最后一个相等：
#           和dp[i-1][j-1]相等
#     2. 最后一个不相等： 三种情况（str1 编辑成 str2 的三种路径）选出一个最小的
#          (1) 1. str1[:-1] -> str2[:-1]
#              2. 替换最后一个  
#          (2) 1. str1[:-1] -> str2
#              2. 删除 str1 最后一个元素
#          (3) 1. str1 - > str2[:-1]
#              2. str1后面加个str2[-1]元素 
#       dp[m][n] 表示长度为 m 的 str1 子串编辑成长度为 n 的 str2 子串的最小代价
        m, n = len(word1), len(word2)
        dp = [[-1] * (n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1] + 1, dp[i][j-1]+1, dp[i-1][j]+1)

        return dp[m][n]

    @solution
    def minDistance(self, word1, word2):
        m, n = len(word1), len(word2)
        cost = [[0 for i in range(n+1)] for i in range(m+1)]
        for i in range(m+1):
            cost[i][0] = i
        for j in range(n+1):
             cost[0][j] = j
        for i in range(1, m+1):
            for j in range(1, n+1):     
                if word1[i-1] == word2[j-1]:
                    cost[i][j] = cost[i-1][j-1]
                else:
                    cost[i][j] = 1 + min(cost[i-1][j-1], cost[i][j-1], cost[i-1][j]) 
        return cost[i][j]    

def main():
    q = Q072()
    q.add_case(q.case('horse', 'ros').assert_equal(3))
    q.add_case(q.case("intention", "execution").assert_equal(5))
    q.run()


if __name__ == '__main__':
    main()
