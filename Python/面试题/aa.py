# 给定一个二维数组ary，数组中的元素为1或0，所有相邻元素（上下左右四相邻）
# 都为1的一个区域为连通区域，请找出最大的连通区域，输出连通区域的大小

# input [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
# output
# 
def maxArea(matrix):
	if not matrix or not matrix[0]:
		return 0

	m, n = len(matrix), len(matrix[0]) 
	memo, max_area = [], 0
	for i in range(m):
	    for j in range(n):
		    v = matrix[i][j]
            if v == 1:
                memo.append((i, j))
                max_area += 1
                if i - 1 >= 0:
                    up = matrix[i-1][j]
                    if up == 1 and (i-1, j) not in memo:
                        memo.append((i-1), j)
                        max_area += 1
                if i + 1 < m:
                    bottom = matrix[i+1][j]
                    if bottom == 1 and (i+1, j) not in memo:
                        memo.append((i+1, j))
                        max_area += 1
                if j - 1 >= 0:
                    left = matrix[i][j-1]
                    if left == 1 and (i, j-1) not in memo:
                        memo.append((i, j-1))
                        max_area += 1
                if j + 1 < n:
                    right = matrix[i][j+1]    
                    if right == 1 and (i, j+1) not in memo:
                        memo.append((i, j+1))      
                        max_area += 1    


if __name__ == "__main__":
    print(maxArea([[0, 1, 0], [1, 1, 1], [0, 1, 0]]))