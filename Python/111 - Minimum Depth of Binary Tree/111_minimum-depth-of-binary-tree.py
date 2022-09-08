from leezy import solution, Solution


class Q111(Solution):
    @solution
    def minDepth(self, root):
        pass


def main():
    q = Q111()
    q.add_case(q.case([3, 9, 20, None, None, 15, 7]))
    q.run()

if __name__ == '__main__':
    main()
