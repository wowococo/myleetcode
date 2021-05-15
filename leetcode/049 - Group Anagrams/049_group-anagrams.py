from leezy import solution, Solution
from collections import Counter


class Q049(Solution):
    @solution
    def groupAnagrams(self, strs):
        # 56ms 77.80%
        ans = []
        memo = {}  # key is sorted_s, value is the index that s in the ans.
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s in memo:
                ans[memo[sorted_s]].append(s)
            else:
                ans.append([s])
                memo[sorted_s] = len(ans) - 1
        
        return ans

            
def main():
    q = Q049()
    q.add_case(q.case([]).assert_equal([]))
    q.add_case(q.case(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']).assert_equal([['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]))
    q.run()


if __name__ == '__main__':
    main()
