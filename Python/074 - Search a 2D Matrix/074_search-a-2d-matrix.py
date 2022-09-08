from leezy import solution, Solution


class Q074(Solution):
    # 32 ms faster than 96.26%, 15.2 MB less than 5.38%
    # 40 ms faster than 68.32%, 15 MB less than 5.38%
    @solution
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1
        while l < r:
            mid = l + (r - l) // 2
            v = matrix[mid // n][mid % n]
            if  v== target:
                return True
            elif v > target:
                r = mid
            else:
                l = mid + 1
        if l == r and matrix[l // n][l % n] == target:
            return True
        return False
    
    @solution
    def searchMatrix2(self, matrix, target):
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        l , r = 0, m * n
        while l < r:
            mid = l + (r - l) // 2
            v = matrix[mid // n][mid % n]
            if v == target:
                return True
            elif v > target:
                r = mid
            else:
                l = mid + 1
        return False


def main():
    q = Q074()
    q.add_case(q.case([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 3).assert_equal(True))
    q.add_case(q.case([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 13).assert_equal(False))
    q.add_case(q.case([], 0).assert_equal(False))
    q.add_case(q.case([[1]], 1).assert_equal(True))
    q.add_case(q.case([[1,3]], 3).assert_equal(True))
    q.run()


if __name__ == '__main__':
    main()
