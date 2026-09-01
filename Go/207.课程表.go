/*
 * @lc app=leetcode.cn id=207 lang=golang
 *
 * [207] 课程表
 */
package main

// @lc code=start
func canFinish(numCourses int, prerequisites [][]int) bool {
	// 课程指向先修课程，形成的图，看有没有环，如果没有环，就可以完成所有课程
	// 如何判断有没有环，使用拓扑排序判断，用到入度、队列和哈希表保存课程和先修课程的关系

	// ingree 用来保存每个节点的入度
	ingree := make([]int, numCourses)
	// 哈希表保存课程和先修课程的关系
	preCourse := make(map[int][]int, numCourses)

	// 遍历prerequisites，维护入度和哈希表
	for _, pre := range prerequisites {
		preCourse[pre[0]] = append(preCourse[pre[0]], pre[1])
		ingree[pre[1]]++
	}

	// 将入度为 0 的存进队列
	count := 0
	queue := make([]int, 0)
	for i := 0; i < numCourses; i++ {
		if ingree[i] == 0 {
			queue = append(queue, i)
			count++
		}
	}

	// BFS拓扑排序
	for len(queue) > 0 {
		front := queue[0]
		queue = queue[1:]
		// 将队首元素的关联的节点的入度都减 1
		for i := 0; i < len(preCourse[front]); i++ {
			nextCourse := preCourse[front][i]
			ingree[nextCourse]--

			// 如果入度有出现==0 的，就加入队列
			if ingree[nextCourse] == 0 {
				queue = append(queue, nextCourse)
				count++
			}
		}
	}

	if count == numCourses {
		return true
	}

	return false
}

// @lc code=end
