from leezy import solution, Solution
from leezy.assists import TreeContext


class Q114(Solution):
    @solution
    def flatten(self, root):
        # iteration
        while root:
            if not root.left:
                root = root.right
            else:
                # find rightmost node of the left subtree
                rm = root.left
                while rm.right:
                   rm = rm.right
                rm.right = root.right
                root.right = root.left
                root.left = None
                
                root = root.right

    @solution
    def flatten_recur(self, root):



def main():
    q = Q114()
    q.set_context(TreeContext)
    q.add_case(q.case([1,2,5,3,4,None,6]))
    q.run()


if __name__ == '__main__':
    main()
