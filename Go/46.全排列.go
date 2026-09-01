/*
 * @lc app=leetcode.cn id=46 lang=golang
 *
 * [46] 全排列
 */
package main

// @lc code=start
func permute(nums []int) [][]int {
	// 回溯的经典运用：全排列
	// 回溯使用递归
	var res [][]int
	var tmp []int // 临时数组存储过程中的每一个数组
	// 在递归的过程中去修改 res，所以传递 res 的指针，因为函数传递的切片是值传递
	dfs(&res, tmp, nums)
	return res
}

// 辅助函数进行递归回溯,像是在走一颗决策树
func dfs(res *[][]int, tmp []int, nums []int) {
	// 递归的终止条件，当 tmp 数组的长度=nums 数组的长度时，当前 tmp 是 res 的一个符合条件的元素
	if len(tmp) == len(nums) {
		// 需要进行深拷贝，不然下面 tmp append 就会影响这里已经 append res 里的
		cp := make([]int, len(tmp))
		copy(cp, tmp)
		*res = append(*res, cp)
		return
	}

	// 遍历数组中的每一个元素
	for i := 0; i < len(nums); i++ {
		// nums 里的元素不能在 tmp 里出现过，因为这道题全排列的元素不相等呀
		j := 0
		for j < len(tmp) {
			if nums[i] == tmp[j] {
				break
			}
			j++
		}

		if j == len(tmp) {
			// 说明当前元素不在 tmp 出现过，将当前元素加入 tmp
			tmp = append(tmp, nums[i])
			//  继续下一个元素的递归
			dfs(res, tmp, nums)
			// 回溯，将上面加入的元素 pop 出来
			tmp = tmp[:len(tmp)-1]
		}
	}

}

// @lc code=end
