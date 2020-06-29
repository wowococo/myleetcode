from leezy import solution, Solution


class Q003(Solution):
    @solution
    def lengthOfLongestSubstring(self, s):
        pass


def main():
    q = Q003()
    q.add_case(q.case('abcabcbb'))
    q.run()

if __name__ == '__main__':
    main()
