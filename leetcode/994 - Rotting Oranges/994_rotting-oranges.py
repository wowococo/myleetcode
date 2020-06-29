from leezy import solution, Solution


class Q994(Solution):
    @solution
    def orangesRotting(self, grid):
        pass


def main():
    q = Q994()
    q.add_case(q.case([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
    q.run()


if __name__ == '__main__':
    main()
