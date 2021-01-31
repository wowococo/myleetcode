from leezy import solution, Solution


class Q1653(Solution):
    @solution
    def minimumDeletions(self, s):
        end_a, end_b = 0, 0
        for char in s:
            if char == "a":
                end_a = end_a
                end_b = end_b + 1
            if char == "b":
                end_b = min(end_a, end_b)
                end_a = end_a + 1
        return min(end_a, end_b)


def main():
    q = Q1653()
    q.add_case(q.case('aababbab'))
    q.run()


if __name__ == '__main__':
    main()
