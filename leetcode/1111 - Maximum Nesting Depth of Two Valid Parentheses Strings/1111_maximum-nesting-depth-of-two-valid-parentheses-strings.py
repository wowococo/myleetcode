from leezy import solution, Solution


class Q1111(Solution):
    @solution
    def maxDepthAfterSplit(self, seq):
        pass


def main():
    q = Q1111()
    q.add_case(q.case('(()())'))
    q.run()


if __name__ == '__main__':
    main()
