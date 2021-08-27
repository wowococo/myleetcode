from leezy import solution, Solution


class Q139(Solution):
    @solution
    def wordBreak(self, s, wordDict):
        # dp[i] 表示长度为 i 的子串 s[0:i]是否能 break
        N = len(s)
        dp = [False] * N
        def canbreak(start):
            if start == N:
                return True
            for i in range(start+1, N+1):
                if dp[s[start:i]] and canbreak(i):
                    return True

        return dp[N]

def main():
    q = Q139()
    q.add_case(q.case('leetcode', ['leet', 'code']))
    q.run()


if __name__ == '__main__':
    main()
