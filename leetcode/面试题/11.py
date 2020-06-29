
def maxArea(height):
    l = 0
    r = len(height)-1
    max_area = min(height[l], height[r]) * (r - l)
    for _ in range(len(height)-1):
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
        area = min(height[l], height[r]) * (r - l)
        if area > max_area: 
                max_area = area
    return max_area
print(maxArea([1,8,6,2,5,4,8,3,7]))