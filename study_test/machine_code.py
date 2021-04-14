
def maxlenEqualK(arr , k ):  
    memo = {0: 0}
    prefix_sum = 0  
    ans = 0
    for i, n in enumerate(arr, 1):
        prefix_sum += n
        if prefix_sum not in memo:
            memo[prefix_sum] = i
        counterpart = prefix_sum - k
        if counterpart in memo:
            ans = max(i - memo[counterpart], ans)
    return ans

if __name__ == "__main__":
    print(maxlenEqualK([1,-2,1,1,1], 0))