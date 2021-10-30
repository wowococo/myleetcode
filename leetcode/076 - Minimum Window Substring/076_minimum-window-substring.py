from collections import defaultdict
from typing import Match
from leezy import solution, Solution
from collections import defaultdict

class Q076(Solution):
    @solution
    def minWindow(self, s, t):
        # 需要两个哈希表，need 存储 t 的每个字符的数量；window 存储窗口中 need 中的字符的数量
        # valid 表示 window 满足包含 need 中所有的数
        i = 0
        res = s
        min_len = float('inf')
        need = defaultdict(int)
        window = defaultdict(int)
        for ch in t:
            need[ch] += 1

        match = 0
        for j in range(len(s)):
            right_ch = s[j]
            if right_ch in need:
                window[right_ch] += 1
                if window[right_ch] == need[right_ch]:
                    match += 1
            
            while match == len(need):
                # 因为求最小，所以每次 x 向右收缩窗口的时候更新一下 res
                if j -i + 1 <= len(res):
                    min_len = j - i + 1
                    res = s[i:j+1]
                left_ch = s[i]
                i += 1
                if left_ch in need:
                    window[left_ch] -= 1
                    if window[left_ch] < need[left_ch]:
                        match -= 1
            
        return res if min_len != float('inf') else ""


def main():
    q = Q076()
    q.add_case(q.case('ADOBECODEBANC', 'ABC').assert_equal('BANC'))
    # 两个比较重要的边界条件
    q.add_case(q.case('a', 'a').assert_equal('a'))
    q.add_case(q.case('a', 'aa').assert_equal(''))
    q.run()


if __name__ == '__main__':
    main()
