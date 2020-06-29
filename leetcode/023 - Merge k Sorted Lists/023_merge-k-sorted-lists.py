from leezy import solution, Solution


class Q023(Solution):
    @solution
    def mergeKLists(self, lists):
        pass


def main():
    q = Q023()
    q.add_case(q.case([[1, 4, 5], [1, 3, 4], [2, 6]]))
    q.run()

if __name__ == '__main__':
    main()
