from leezy import solution, Solution


class Q079(Solution):
    @solution
    def exist(self, board, word):
        #  4060 ms , 59.38%
        if not board:
            return False
        if not board[0]:
            return False
        if not word:
            return True

        M, N = len(board), len(board[0])
        for i in range(M):
            for j in range(N):
                if self.dfs(board, word, i, j):
                    return True
        return False

    def dfs(self, board, suffix, x, y):
        if suffix == "":
            return True
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or suffix[0] != board[x][y]:
            return False

        tmp = board[x][y]
        board[x][y] = "#"
        nxt_suffix = suffix[1:]
        found = (self.dfs(board, nxt_suffix, x+1, y) or
                self.dfs(board, nxt_suffix, x-1, y) or
                self.dfs(board, nxt_suffix, x, y-1) or
                self.dfs(board, nxt_suffix, x, y+1))

        board[x][y] =tmp
        return found

def main():
    q = Q079()
    q.add_case(q.case([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'ABCCED'))
    q.add_args([['a', 'a']], 'aaa')
    q.add_args([["a", "a", "a", "a"],
                ["a", "a", "a", "a"]], "aaaaaaaaa")
    q.add_args([["A", "B", "C", "E"],
                ["S", "F", "E", "S"],
                ["A", "D", "E", "E"]], "ABCESEEEFS")
    q.run()


if __name__ == '__main__':
    main()
