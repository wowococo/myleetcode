from leezy import solution, Solution
from leezy.assists import TreeContext

class Q098(Solution):
    @solution
    def isValidBST(self, root):
        # bst 左子树都比根节点小，右子树都比根节点大
        # bst 的特性： 中序遍历是一个有序的数组,所以最简单的方式就是中序遍历一下看是否是个有序的数组依次判断
        nums = []
        def inorder(node):
            if node is None: return []
            inorder(node.left)
            nums.append(node.val)
            inorder(node.right)
        
        inorder(root)
        for x, y in zip(nums, nums[1:]):
            if x >= y:
                return False
        return True

        



def main():
    q = Q098()
    q.set_context(TreeContext)
    q.add_case(q.case([2, 1, 3]))
    q.add_case(q.case([5,1,4,None,None,3,6]))
    q.run()


if __name__ == '__main__':
    main()
