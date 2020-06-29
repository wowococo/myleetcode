from leezy import solution, Solution
from collections import deque
from leezy.assists import TreeContext


class Q199(Solution):
    # @solution
    # def rightSideView(self, root):
    #     if not root:
    #         return []
    #     result = []
    #     # use deque was thinked complicated.
    #     q = deque()
    #     q.append(root)
    #     while q:
    #         size = len(q)
    #         for i in range(size):
    #             node = q.popleft()
    #             if node.left:
    #                 q.append(node.left)
    #             if node.right:
    #                 q.append(node.right)
    #             if i == size - 1:
    #                 result.append(node.val)
    #     return result

    @solution
    def rightSideView(self, root):
        # python is easier than Java.
        if not root:
            return []
        result = []
        level = [root]
        while level:
            result.append(level[-1].val)
            next_level = []
            for node in level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            level = next_level
        return result


def main():
    q = Q199()
    q.set_context(TreeContext)
    q.add_case(q.case([1, 2, 3, None, 5, None, 4]))

    q.run()


if __name__ == '__main__':
    main()
