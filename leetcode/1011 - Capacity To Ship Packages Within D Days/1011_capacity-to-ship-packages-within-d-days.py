from leezy import solution, Solution


class Q1011(Solution):
    @solution
    def shipWithinDays(self, weights, D):
        pass


def main():
    q = Q1011()
    q.add_case(q.case([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
    q.run()


if __name__ == '__main__':
    main()
