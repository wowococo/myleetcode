from leezy import solution, Solution


class Q1024(Solution):
    @solution
    def videoStitching(self, clips, T):
        pass


def main():
    q = Q1024()
    q.add_case(q.case([[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]], 10))
    q.run()

if __name__ == '__main__':
    main()
