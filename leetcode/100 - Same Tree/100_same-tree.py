from leezy import solution, Solution


class Q100(Solution):
    @solution
    def isSameTree(self, p, q):
        pass


def main():
    q = Q100()
    q.add_case(q.case([1, 2, 3], [1, 2, 3]))
    q.run()


if __name__ == '__main__':
    main()
