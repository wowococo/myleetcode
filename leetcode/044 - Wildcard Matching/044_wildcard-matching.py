from leezy import solution, Solution


class Q044(Solution):
    @solution
    def isMatch(self, s, p):
        pass


def main():
    q = Q044()
    q.add_case(q.case('aa', 'a'))
    q.run()


if __name__ == '__main__':
    main()
