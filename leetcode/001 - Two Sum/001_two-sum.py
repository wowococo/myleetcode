from leezy import solution, Solution


class Q001(Solution):
    @solution
    def twoSum(self, nums, target):
        pass


def main():
    q = Q001()
    q.add_case(q.case([2, 7, 11, 15], 9))
    q.run()

if __name__ == '__main__':
    main()
