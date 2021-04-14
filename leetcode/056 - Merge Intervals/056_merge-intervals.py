from leezy import solution, Solution


class Q056(Solution):
    @solution
    def merge(self, intervals):
        pass


def main():
    q = Q056()
    q.add_case(q.case([[1, 3], [2, 6], [8, 10], [15, 18]]))
    q.run()


if __name__ == '__main__':
    main()
