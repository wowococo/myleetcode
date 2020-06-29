from leezy import solution, Solution


class Q072(Solution):
    @solution
    def minDistance(self, word1, word2):
        m, n = len(word1), len(word2)
        cost = [[0 for i in range(n+1)] for i in range(m+1)]
        for i in range(m+1):
            cost[i][0] = i
        for j in range(n+1):
             cost[0][j] = j
        for i in range(1, m+1):
            for j in range(1, n+1):     
                if word1[i-1] == word2[j-1]:
                    cost[i][j] = cost[i-1][j-1]
                else:
                    cost[i][j] = 1 + min(cost[i-1][j-1], cost[i][j-1], cost[i-1][j]) 
        return cost[i][j]    
def main():
    q = Q072()
    q.add_case(q.case('horse', 'ros'))
    q.add_case(q.case("intention", "execution"))
    q.run()


if __name__ == '__main__':
    main()
