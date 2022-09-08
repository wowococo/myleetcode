from leezy import solution, Solution


class Q892(Solution):
    @solution
    def surfaceArea(self, grid):
        pass


def main():
    q = Q892()
    q.add_case(q.case([[2]]))
    q.run()


if __name__ == '__main__':
    main()
