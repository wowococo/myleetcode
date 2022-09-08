from leezy import solution, Solution


class Q289(Solution):
    @solution
    def gameOfLife(self, board):
        # 0: 00: dead <- dead 
        # 1: 01: dead <- live
        # 2: 10: live <- dead
        # 3: 11: live <- live 
        if not board:
            return 
        neighbors = [(1,0),(-1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                count = 0
                for neighbor in neighbors:
                    x = neighbor[0]+i
                    y = neighbor[1]+j
                    if -1 < x < m and -1 < y < n:
                        count += board[x][y] & 1
                if board[i][j] == 1:
                    if 2 <= count <= 3:
                        board[i][j] = 3
                else:
                    if count == 3:
                        board[i][j] = 2

        # 替换
        for i in range(m):
            for j in range(n):
                    board[i][j] >>= 1

        return board
        


def main():
    q = Q289()
    q.add_case(q.case([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]))
    q.run()


if __name__ == '__main__':
    main()
