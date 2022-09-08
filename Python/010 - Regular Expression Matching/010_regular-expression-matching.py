from leezy import solution, Solution


class Q010(Solution):
    @solution
    def isMatch(self, s, p):
        pass


def main():
    q = Q010()
    q.add_case(q.case('aa', 'a'))
    q.run()


if __name__ == '__main__':
    main()
