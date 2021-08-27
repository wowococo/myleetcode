from leezy import solution, Solution


class Q778(Solution):
    @solution
    def swimInWater(self, grid):
        pass


def main():
    q = Q778()
    q.add_case(q.case([[0, 2], [1, 3]]))
    q.run()


if __name__ == '__main__':
    main()
