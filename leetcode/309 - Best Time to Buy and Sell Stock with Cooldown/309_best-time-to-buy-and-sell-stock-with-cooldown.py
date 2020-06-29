from leezy import solution, Solution


class Q309(Solution):
    @solution
    def maxProfit(self, prices):
        pass


def main():
    q = Q309()
    q.add_case(q.case([1, 2, 3, 0, 2]))
    q.run()

if __name__ == '__main__':
    main()
