from leezy import solution, Solution


class Q561(Solution):
    @solution
    def arrayPairSum(self, nums):
        return sum(sorted(nums)[::2])


def main():
    q = Q561()
    q.add_case(q.case([1, 4, 3, 2]))
    q.run()

if __name__ == '__main__':
    main()
