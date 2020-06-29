from leezy import solution, Solution


class Q466(Solution):
    @solution
    def getMaxRepetitions(self, s1, n1, s2, n2):
        pass


def main():
    q = Q466()
    q.add_case(q.case('acb', 4, 'ab', 2))
    q.run()


if __name__ == '__main__':
    main()
