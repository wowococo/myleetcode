from leezy import solution, Solution


class Q043(Solution):
    @solution
    def multiply(self, num1, num2):
        pass


def main():
    q = Q043()
    q.add_case(q.case('2', '3'))
    q.run()


if __name__ == '__main__':
    main()
