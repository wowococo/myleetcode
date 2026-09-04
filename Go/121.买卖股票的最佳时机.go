/*
 * @lc app=leetcode.cn id=121 lang=golang
 *
 * [121] 买卖股票的最佳时机
 */
package main

// @lc code=start
func maxProfit(prices []int) int {
	// 以每个点作为卖出价格，维护它前面的最小买入价格，
	// 两者相减 = 利润，再维护一个最大利润不断更
	//
	buyPrice := prices[0]
	maxProfit := 0
	for i := 1; i < len(prices); i++ {
		// 这种情况，proflt = 就是负数，还没 0大，
		// 所以不用去计算，直接更新最小买入价格就行了
		if prices[i] < buyPrice {
			buyPrice = prices[i]
		} else {
			profit := prices[i] - buyPrice
			maxProfit = max(maxProfit, profit)
		}
	}

	return maxProfit
}

// @lc code=end
