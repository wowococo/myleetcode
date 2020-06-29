from leezy import solution, Solution


class Q062(Solution):
    @solution
    def uniquePaths(self, m, n):
        pass


def main():
    q = Q062()
    q.add_case(q.case(3, 2))
    q.run()


if __name__ == '__main__':
    main()
