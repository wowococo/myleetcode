from leezy import solution, Solution


class Q287(Solution):
    @solution
    def findDuplicate(self, nums):
        pass



def main():
    q = Q287()
    q.add_case(q.case([1, 3, 4, 2, 2]))
    q.run()


if __name__ == '__main__':
    main()
