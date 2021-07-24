from leezy import solution, Solution


class Q207(Solution):
    @solution
    def canFinish(self, numCourses, prerequisites):
        # 32ms, 99.26%
        UNKNOWN, VISITING, VISITED = 0, 1, 2
        states = [UNKNOWN] * numCourses
        adj = [[] for _ in range(numCourses)]
        for edge in prerequisites:
            adj[edge[0]].append(edge[1])
        # 判断有没有环
        def dfs(v):
            if states[v] == VISITED:
                return False
            if states[v] == VISITING:
                return True
            states[v] = VISITING
            for w in adj[v]:
                if dfs(w):
                    return True
            states[v] = VISITED
            return False
        for v in range(numCourses):
            if dfs(v):
                return False
        return True
        

def main():
    q = Q207()
    q.add_case(q.case(2, [[1, 0]]))
    q.add_case(q.case(8, [[1,0],[2,6],[1,7],[6, 4], [7,0], [0,5]]))
    q.add_case(q.case(8, [[1,0],[2,6],[1,7],[5,1],[6,4],[7,0],[0,5]]))
    q.run()


if __name__ == '__main__':
    main()
