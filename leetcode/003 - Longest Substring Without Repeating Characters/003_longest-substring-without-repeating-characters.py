from leezy import solution, Solution


class Q003(Solution):
    @solution
    def lengthOfLongestSubstring(self, s):
        # hashtable and sliding window, recommend huahua
        # 72ms 70.58%
        memo = {}
        i = 0
        max_len = 0
        for j in range(len(s)):
            if s[j] in memo:
                i = max(i, memo[s[j]]+1)
            max_len = max(max_len, j-i+1)
            memo[s[j]] = j
        return max_len

def main():
    q = Q003()
    q.add_case(q.case('abcabcbb').assert_equal(3))
    q.add_case(q.case('abbcabcbb').assert_equal(3))
    q.run()

if __name__ == '__main__':
    main()
