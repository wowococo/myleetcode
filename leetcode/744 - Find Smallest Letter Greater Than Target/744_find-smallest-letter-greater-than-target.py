from leezy import solution, Solution


class Q744(Solution):
    @solution
    def nextGreatestLetter(self, letters, target):
        ord(target)
        l = 0
        r = len(letters) - 1
        while l < r:
            mid = l + (r - l) // 2
            if ord(target) < ord(letters[mid]):
                r = mid
            else:
                l = mid + 1
        if letters[l] > target:
            return letters[l]
        else:
            return letters[l + 1] if l+1 < len(letters) else letters[0]

def main():
    q = Q744()
    q.add_case(q.case(['c', 'f', 'j'], 'a').assert_equal('c'))
    q.add_case(q.case(['c', 'f', 'j'], 'c').assert_equal('f'))
    q.add_case(q.case(['c', 'f', 'j'], 'd').assert_equal('f'))
    q.add_case(q.case(['c', 'f', 'j'], 'g').assert_equal('j'))
    q.add_case(q.case(['c', 'f', 'j'], 'j').assert_equal('c'))
    q.add_case(q.case(['c', 'f', 'j'], 'k').assert_equal('c'))
    q.add_case(q.case(["e","e","e","e","e","e","n","n","n","n"], "e").assert_equal("n"))
                        # 0,  1,  2,  3,  4,  5,  6,  7,  8,  9  
    q.run()


if __name__ == '__main__':
    main()
