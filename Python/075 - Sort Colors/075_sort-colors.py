from leezy import solution, Solution


class Q075(Solution):
    @solution
    def sortColors(self, nums):
        pass


def main():
    q = Q075()
    q.add_case(q.case([2, 0, 2, 1, 1, 0]))
    q.run()


if __name__ == '__main__':
    main()
