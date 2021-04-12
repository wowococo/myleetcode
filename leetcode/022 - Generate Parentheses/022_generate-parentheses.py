from leezy import solution, Solution


class Q022(Solution):
    @solution
    def generateParenthesis(self, n):
        # 36ms 90.38%
        # 组合模板  由于字符串的特殊性，产生一次拼接会生成新的对象，因此无需像其他组合模板一样需要cur.pop()来回溯
        total = []
        # l, r 分别代表 '(',')'的个数
        def dfs(l, r, cur):
            if len(cur) == n * 2:
                total.append(cur)
                return
            if l < n:
                dfs(l+1, r, cur+'(')
            if l > r:
                dfs(l, r+1, cur+')')
        dfs(0, 0, '')
        return total

            
def main():
    q = Q022()
    q.add_case(q.case(3).assert_equal( ['((()))', '(()())', '(())()', '()(())', '()()()']))
    q.run()


if __name__ == '__main__':
    main()
