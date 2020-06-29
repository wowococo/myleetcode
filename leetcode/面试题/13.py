def movingCount(m: int, n: int, k: int) -> int:
    if k < 0:
        return 
    neighbors = [(1, 0)]
    count = 0
    # import pdb; pdb.set_trace()

    for j in range(0, n):
        if j <= k:
            count += 1
    for i in range(m):
        for j in range(n):
            for neighbor in neighbors:
                x = i + neighbor[0]
                y = j + neighbor[1]
                if -1 < x < m and -1 < y < n:
                    if (x // 10 + x % 10 + y // 10 + y % 10) > k:
                        pass
                    else:
                        count += 1
    return count

result1 = movingCount(2, 3, 1)
result2 = movingCount(3, 1, 0)
result3 = movingCount(1, 2, 1)
result4 = movingCount(11, 8, 16)
result5 = movingCount(16, 8, 4)

print(result1, result2, result3, result4, result5)