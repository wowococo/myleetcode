from leezy import solution, Solution


class Q107(Solution):
    @solution
    def levelOrderBottom(self, root):
        pass


def main():
    q = Q107()
    q.add_case(q.case([3, 9, 20, None, None, 15, 7]))
    q.run()

if __name__ == '__main__':
    main()
