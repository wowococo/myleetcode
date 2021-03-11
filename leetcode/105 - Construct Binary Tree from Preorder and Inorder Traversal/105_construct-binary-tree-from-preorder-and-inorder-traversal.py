from leezy import solution, Solution
from leezy.assists import TreeContext, TreeNode
from collections import deque

class Q105(Solution):
    @solution
    def buildTree(self, preorder, inorder):
        
        def reconstruct(preorder, inorder, stop):
            if inorder[0] == stop: return None  # 递归终止条件
            root = TreeNode(preorder.popleft())     # 创建根结点，并消耗掉先序遍历流中的根
            print(preorder, '                    ', inorder)
            root.left = reconstruct(preorder, inorder, root.val)
                                        # 重建左子树，直到在中序遍历流中遇到当前层的根
            inorder.popleft()            # 消耗掉中序遍历流中的根
            root.right = reconstruct(preorder, inorder, stop)
                                        # 重建右子树，直到在中序遍历流中遇到上层的根
            return root                  # 返回重建结果
        
        return reconstruct(deque(preorder + [None]), deque(inorder + [None]), None)

    

def main():
    q = Q105()
    q.add_case(q.case([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]))
    q.run()


if __name__ == '__main__':
    main()
