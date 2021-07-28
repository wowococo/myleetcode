from leezy import solution, Solution


class Q048(Solution):
    @solution
    def rotate(self, matrix):
        # 24 ms , 98.65%
        N = len(matrix)
        for i in range(N):
            for j in range(i+1, N):
               matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for row in matrix:
            row.reverse()
        return matrix


def main():
    q = Q048()
    q.add_case(q.case([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    q.run()


if __name__ == '__main__':
    main()
