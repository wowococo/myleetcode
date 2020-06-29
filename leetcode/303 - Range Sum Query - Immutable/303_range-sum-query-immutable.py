import itertools
class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sums = [0, *itertools.accumulate(nums)]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return (self.sums[j+1]-self.sums[i])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

def main():
    numarray = NumArray([-2, 0, 3, -5, 2, -1])
    operations = ['sumRange', 'sumRange', 'sumRange']
    oprands = [[0, 2], [2, 5], [0, 5]]
    for opt, opd in zip(operations, oprands):
        if hasattr(numarray, opt):
            print(getattr(numarray, opt).__call__(*opd))


if __name__ == '__main__':
    main()
