from leezy import solution, Solution


class Q124(Solution):
    @solution
    def maxPathSum(self, root):
        pass


def main():
    q = Q124()
    q.add_case(q.case([1, 2, 3]))
    q.run()


if __name__ == '__main__':
    main()
