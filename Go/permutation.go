package main

func permute(nums []int) [][]int {
	cur, total := make([]int, 0), make([][]int, 0)
	used := make([]bool, len(nums))
	dfs(len(nums), cur, &total, nums, used)
	return total

}

func dfs(n int, cur []int, total *[][]int, nums []int, used []bool) {
	if len(cur) == n {
		*total = append(*total, cur)
		return
	}
	for i, _ := range nums {
		if used[i] == true {
			continue
		}
		cur = append(cur, nums[i])
		used[i] = true
		dfs(n, cur, total, nums, used)
		cur = cur[:len(cur)-1]
		used[i] = false
	}
}

// 设计一个任务，这个任务里包含 100 个子任务（goroutine完成）。需要实现任务的创建、删除、更新、暂停、启动。
// 一个任务如果不被删除，那么它的子任务会在系统里一直存在。
// 当创建任务的时候，需要创建这 100 个子任务。
// 当删除任务的时候，需要删除这 100 个子任务。
// 当更新任务的时候，需要删除一些已有的子任务，新建一些子任务，此时任务数量可以不是 100。
// 当暂停任务的时候，需要暂停这 100 个子任务。
// 当重新启动任务的时候，需要重新启动这 100 个子任务。
// package main

// type JobInfo struct {
// 	ID int
// 	Name string
// 	JobStatus int
// }
// //
// func Create() {

// }
