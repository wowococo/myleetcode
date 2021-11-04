from leezy import solution, Solution


class Q746(Solution):
    @solution
    def minCostClimbingStairs(self, cost):
        s1 = s2 = 0
        for i in range(len(cost)):
            c = min(s1, s2) + cost[i]
            s1 = s2
            s2 = c
        return min(s1, s2)

def main():
    q = Q746()
    q.add_case(q.case([0, 0, 0, 0]))
    q.add_case(q.case([10, 15, 20]))
    q.add_case(q.case([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
    q.run()


if __name__ == '__main__':
    main()
