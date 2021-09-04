from leezy import solution, Solution


class Q139(Solution):
    @solution
    def wordBreak(self, s, wordDict):
        # 递归，dfs(i) 表示以 s[i:] 能否被拆分为一个或多个在字典中出现的单词。
        # TLE, 35/45
        def dfs(i):
            if i >= len(s):
                return True
            for j in range(i, len(s)):
                if s[i:j+1] in wordDict and dfs(j+1):
                    return True
            
            return False
        
        return dfs(0)

    @solution
    def work_break(self, s, wordDict):
        # TLE 35/45 和上面一样，将 list 转为 set 这复杂度降低了
        wordDict = set(wordDict)
        def dfs(i):
            if i >= len(s):
                return True
            for j in range(i, len(s)):
                if s[i:j+1] in wordDict and dfs(j+1):
                    return True

            return False

        return dfs(0)

    @solution
    def work_break_memo(self, s, wordDict):
        # 记忆化递归, memo 的每个位置的值存储 s[i:] 是否可以被单词拆分
        # 40ms 68.32%
        memo = [None] * len(s)
        wordDict = set(wordDict)
        def dfs(i):
            # i 越界，
            if i >= len(s):
                return True
            if memo[i] is not None:
                return memo[i]
            for j in range(i, len(s)):
                if s[i:j+1] in wordDict and dfs(j+1):
                    memo[i] = True
                    return True

            memo[i] = False
            return False
        
        return dfs(0)

    @solution
    def wordBreakMemo(self, s, wordDict):
        word_dict = set(wordDict)
        memo = {}
        # dfs(i，) 表示的意思和上面是一样的， s[i:] 是否能够被 break
        def dfs(i, formed):
            if i >= len(s):
                return formed == ""
            if i in memo:
                return memo[i]
            for j in range(i, len(s)):
                formed += s[j]
                if formed in wordDict and dfs(j+1, ""):
                    return True

            memo[i] = False
            return False

        return dfs(0, "")

    @solution
    def word_break_dp(self, s, wordDict):
        # dp[i] 表示长度为 i 的 s[0:i] 是否能被拆分为单词
        # 32ms 94.8%
        wordDict = set(wordDict)
        N = len(s)
        dp = [False] * (N+1)
        dp[0] = True
        for i in range(1, N+1):
            # j is to split i
            for j in range(0, i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[N]

def main():
    q = Q139()
    q.add_case(q.case('leetcode', ['leet', 'code']).assert_equal(True))
    q.add_case(q.case("applepenapple", ["apple", "pen"]).assert_equal(True))
    q.add_case(q.case('catsandog', ["cats", "dog", "sand", "and", "cat"]).assert_equal(False))
    q.run()


if __name__ == '__main__':
    main()
