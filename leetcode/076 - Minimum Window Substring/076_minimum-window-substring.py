from leezy import solution, Solution


class Q076(Solution):
    @solution
    def minWindow(self, s, t):
        pass


def main():
    q = Q076()
    q.add_case(q.case('ADOBECODEBANC', 'ABC'))
    q.run()


if __name__ == '__main__':
    main()
