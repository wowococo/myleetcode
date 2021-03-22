from leezy import solution, Solution


class Q005(Solution):
    @solution
    def longestPalindrome(self, s):
        # dp[i][j] 表示s[i..j]是否是回文子串。s[i..j]是左闭右闭区间。
        start = 0
        max_len = 1
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for j in range(1, n):
            for i in range(j):
                if s[i] == s[j]:
                    if j - i < 3:
                        dp[i][j] = True   # 当子串的长度为2或者3的时候若满足s[i]==s[j],可直接判定为True； j-i+1 < 4
                    else:
                        dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = False

                if dp[i][j]:
                    cur_len = j - i + 1
                    if cur_len > max_len:
                        max_len = cur_len
                        start = i
        
        return s[start:start+max_len]
            
            
       
    


def main():
    q = Q005()
    q.add_case(q.case('babad').assert_equal('bab'))
    q.add_case(q.case("abb").assert_equal("bb"))
    q.add_case(q.case("aaaa").assert_equal("aaaa"))
    q.run()


if __name__ == '__main__':
    main()
