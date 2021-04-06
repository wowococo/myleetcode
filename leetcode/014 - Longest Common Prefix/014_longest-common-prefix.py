from leezy import solution, Solution


class Q014(Solution):
    @solution
    def longestCommonPrefix(self, strs):
        # 40ms 74.27%
        if not strs:
            return ""
        strs = sorted(strs, key=len)
        short_s = strs[0]
        for i in range(len(short_s), 0, -1):
            count = 0
            short_s = short_s[:i]
            for s in strs[1:]:
                if short_s == s[:len(short_s)]:
                    count += 1
                else:
                    break
            if count == len(strs)-1:
                return short_s
        return ""


def main():
    q = Q014()
    q.add_case(q.case(['flower', 'flow', 'flight']).assert_equal('fl'))
    q.add_case(q.case(["dog","racecar","car"]).assert_equal(''))
    q.add_case(q.case(["abca","abc","abca","abc","abcc"]).assert_equal("abc"))
    q.add_case(q.case(["reflower","flow","flight"]).assert_equal(""))
    q.run()


if __name__ == '__main__':
    main()
