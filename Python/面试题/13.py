def binary_search(arr, tar):
    n = len(arr)
    l, r = 0, n
    while l < r:
        m = l + (r - l) // 2
        v = arr[m]
        if v == tar:
            return m
        elif v < tar:
            l = m + 1
        else:
            r = m

    return -1


if __name__ == "__main__":
    assert(binary_search([1,2,3,4,5], 3)) == 2
    assert(binary_search([1,2,3], 4)) == -1