from leezy import solution, Solution
from leezy.assists import TreeNode

class Q108(Solution):
    @solution
    def sortedArrayToBST(self, nums):
        # 所谓二叉搜索树 ，就是左子树节点值都小于根节点值 ，右子树所有节点值都大于根节点，左右子树分别都是二叉搜索树。
        # 构建二叉搜索树，选取数字中任意一个值都可以作为根节点，这个数左边的就是左子树的节点值，右边的就是右子树的节点值，
        # 但这个题还要求平衡，高度不能相差为 1，那么我们就选取数组中间位置的数作为根结点的值。
        # 先左子树递到叶子节点为止，然后归的过程就是依次向上返回每一个结点；然后右子树
        l, r = 0, len(nums) - 1
        
        def bst(l, r):
            if l > r:
                return
            mid = l + (r - l) // 2
            root = TreeNode(nums[mid])
            root.left = bst(l, mid-1)
            root.right = bst(mid+1, r)
            return root
        return bst(l, r)


def main():
    q = Q108()
    q.add_case(q.case([-10, -3, 0, 5, 9]))
    q.run()


if __name__ == '__main__':
    main()
