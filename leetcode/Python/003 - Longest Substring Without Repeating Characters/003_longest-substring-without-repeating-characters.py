from leezy import solution, Solution
from collections import defaultdict

class Q003(Solution):
    @solution
    def length_of_longest_substring(self, s):
        # 遇见子串首先要想到滑动窗口,这道题valid是含有重复字符的时候
        i, j = 0, 0
        # memo 存储窗口里遇见字符的数量
        memo = defaultdict(int)
        res = 0
        for j in range(len(s)):
            right = s[j]
            memo[right] += 1
            while memo[right] > 1:
                left = s[i]
                memo[left] -= 1
                i += 1
            
            # 因为求的是最长子串，所以在每次j 向右扩展窗口的时候判断一下 res
            res = max(res, j-i+1)
        return res

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
    
    @solution
    def lengthOfLongestSubstring_(self, s):
        memo = {}
        i = 0
        max_len = 0
        for j, x in enumerate(s):
            if x in memo:
                i = max(i, memo[x]+1)
            max_len = max(max_len, j-i+1)
            memo[x] = j
        return max_len

def main():
    q = Q003()
    q.add_case(q.case('abcabcbb').assert_equal(3))
    q.add_case(q.case('abbcabcbb').assert_equal(3))
    q.run()

if __name__ == '__main__':
    main()
