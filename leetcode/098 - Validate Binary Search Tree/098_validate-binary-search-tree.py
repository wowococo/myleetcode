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
    
    @solution
    def isValidBST_better(self, root):
        # 上个解法用了额外的空间O(n), 可尝试优化，即在中序遍历递归的过程中判断
        self.prev = None

        def walk(node):
            if node is None: return True
            if not walk(node.left):
                return False
            if self.prev is not None and self.prev >= node.val:
                return False
            self.prev = node.val
            if not walk(node.right):
                return False
            return True
        
        return walk(root)


def main():
    q = Q098()
    q.set_context(TreeContext)
    q.add_case(q.case([2, 1, 3]))
    q.add_case(q.case([5,1,4,None,None,3,6]))
    q.run()


if __name__ == '__main__':
    main()
