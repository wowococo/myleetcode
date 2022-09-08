from leezy import solution, Solution


class Q273(Solution):
    @solution
    def numberToWords(self, num):
        pass


def main():
    q = Q273()
    q.add_case(q.case(123))
    q.run()


if __name__ == '__main__':
    main()
