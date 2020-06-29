from leezy import solution, Solution


class Q200(Solution):
    @solution
    def numIslands(self, grid):
        island_nums = 0 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.infect(grid, i, j)
                    island_nums += 1
        return island_nums

    def infect(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != "1":    
            return
        grid[i][j] = "2"
        self.infect(grid, i-1, j)
        self.infect(grid, i+1, j)
        self.infect(grid, i, j-1)
        self.infect(grid, i, j+1)


def main():
    q = Q200()
    q.add_case(q.case([['1', '1', '1', '1', '0'], ['1', '1', '0', '1', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '0', '0', '0']]))
    q.add_case(q.case([['1', '1', '0', '0', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '1', '0', '0'], ['0', '0', '0', '1', '1']]))
    q.run()


if __name__ == '__main__':
    main()
