from leezy import solution, Solution


class Q198(Solution):
    @solution
    def rob(self, nums):
        pass


def main():
    q = Q198()
    q.add_case(q.case([1, 2, 3, 1]))
    q.run()


if __name__ == '__main__':
    main()
