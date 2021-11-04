from leezy import solution, Solution


class Q005(Solution):
    @solution
    def longest_palindrome(self, s):
        # 寻找回文子串的核心思想是使用双指针从“中间”向两边扩散来判断回文子串，这个中间可以是 s 的任意一个字符,
        # 要有一个函数来求出i，j 开始的回文子串，之所以用两个指针i，j是因为可以同时兼顾到字符的长度可能为奇数或者偶数
        def polindrome(l, r):
            pd = ""
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    pd = s[l:r+1]
                    l -= 1
                    r += 1
                else:
                    return pd
            
            return pd
        
        res = ""
        for i in range(len(s)):
            odd = polindrome(i, i)
            even = polindrome(i, i+1)

            res = max(res, odd, even, key=len)
        
        return res


    @solution
    def longestPalindrome(self, s):
        # dp[i][j] 表示s[i..j]是否是回文子串。s[i..j]是左闭右闭区间。这个动态规划也太麻烦了吧
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
    q.add_case(q.case("cbbd").assert_equal("bb"))
    q.run()


if __name__ == '__main__':
    main()
