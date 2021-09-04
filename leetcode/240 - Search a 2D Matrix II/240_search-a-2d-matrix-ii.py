from leezy import solution, Solution


class Q240(Solution):
    @solution
    def searchMatrix(self, matrix, target):
        # 160ms 58.87%
        if not matrix or not matrix[0]:
            return False
        # i 代表行的最小值，j 代表列的最大值 
        i, j = 0, len(matrix[0])-1
        while i < len(matrix) and j >= 0:
            v = matrix[i][j]
            if v == target:
                return True
            if v < target:
                i += 1
            else:
                j -= 1

        return False 

    @solution
    def search_matrix_II(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        # i 表示行的最大值，j 表示列的最小值
        i, j = len(matrix) - 1, 0
        while i >= 0 and j < len(matrix[0]):
            v = matrix[i][j]
            if v == target:
                return True
            elif v < target:
                j += 1
            else:
                i -= 1

        return False

def main():
    q = Q240()
    q.add_case(q.case([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 5))
    q.add_case(q.case([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20))
    q.add_case(q.case([[-1,3]], -1))
    q.run()


if __name__ == '__main__':
    main()
