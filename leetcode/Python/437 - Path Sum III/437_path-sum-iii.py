from leezy import solution, Solution
from leezy.assists import TreeContext


class Q437(Solution):
    @solution
    def pathSum(self, root, targetSum):
        if root is None: return 0
        


def main():
    q = Q437()
    q.set_context(TreeContext)
    q.add_case(q.case([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1], 8))
    q.run()


if __name__ == '__main__':
    main()
