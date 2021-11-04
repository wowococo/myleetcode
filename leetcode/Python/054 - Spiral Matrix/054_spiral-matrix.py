from leezy import solution, Solution


class Q054(Solution):
    @solution
    def spiralOrder(self, matrix):
        if not matrix: return []
        ans = []
        i, j = 0, 0  #  i, j表示矩阵两个维度的起点
        m, n = len(matrix), len(matrix[0])  # m, n表示行数、列数，也是这个矩阵每列、每行的元素个数
        while m > 1 and n > 1:
            ans.extend(matrix[i][k] for k in range(j, j+n))  # n个
            ans.extend(matrix[k][j+n-1] for k in range(i+1, i+1+m-1))   # m-1个
            ans.extend(matrix[i+m-1][k] for k in reversed(range(j, j+n-1))) # n-1个
            ans.extend(matrix[k][j] for k in reversed(range(i+1, i+1+m-2)))  # m-2个 
            i += 1
            j += 1
            m -= 2
            n -= 2
        
        if m == 1:
            ans.extend(matrix[i][k] for k in range(j, j+n))   # n
        elif n == 1:   # 不能写成 if(考虑到一个元素既是一行也是一列，但这种情况走一次就行了), 也不能写成 else(语法错误)
            ans.extend(matrix[k][j] for k in range(i, i+m))  # m
        
        return ans

    @solution
    def spiralOrder_review(self, matrix):
        if not matrix: return []
        ans = []
        m, n = len(matrix), len(matrix[0])
        i, j = 0, 0
        while m >1 and n > 1:
            ans.extend(matrix[i][k] for k in range(j, j+n)) # n
            ans.extend(matrix[k][j+n-1] for k in range(i+1, i+1+m-1)) # m-1
            ans.extend(matrix[i+m-1][k] for k in reversed(range(j, j+n-1)))  # n-1
            ans.extend(matrix[k][j] for k in reversed(range(i+1, i+1+m-2)))  # m-2
            
            i += 1
            j += 1
            m -= 2
            n -= 2
        
        if m == 1:
            ans.extend(matrix[i][k] for k in range(j, j+n))  # n 
        elif n == 1:
            ans.extend(matrix[k][j] for k in range(i, i+m))  # m
        
        return ans

def main():
    q = Q054()
    q.add_case(q.case([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).assert_equal([1, 2, 3, 6, 9, 8, 7, 4, 5] ))
    q.run()


if __name__ == '__main__':
    main()
