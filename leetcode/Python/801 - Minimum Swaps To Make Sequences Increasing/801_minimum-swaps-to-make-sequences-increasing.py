from leezy import solution, Solution


class Q801(Solution):
    @solution
    def minSwap(self, A, B):
        n = len(A)
        keep[i] = 0
        swap[i] = 1
        for i in range(1,n):
            if A[i] < A[i-1] & B[i] > B[i-1]:
                keep[i] = keep[i-1]
                swap[i] = swap[i-1] + 1
            if A[i] < B[i-1] & B[i] > A[i-1]:
                keep[i] = min(keep[i-1] + 1, swap[i])
                swap[i] = min(swap[i-1], keep[i])
        return min(keep.back(), swap.back())

            
                
def main():
    q = Q801()
    q.add_case(q.case([1, 3, 5, 4], [1, 2, 3, 7]).assert_equal(1))
    q.run()

if __name__ == '__main__':
    main()
