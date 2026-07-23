package main

import (
	"fmt"
	"strconv"
	"strings"
)

func countBirthdayGifts(targetMonth int, employees []string, dates []string) int {
	empBirthMap := make(map[string]int)
	for i := 0; i < len(employees); i++ {
		emp := employees[i]
		dateStr := dates[i]

		dateParts := strings.Split(dateStr, "/")
		if len(dateParts) < 2 {
			continue
		}

		month, err := strconv.Atoi(dateParts[1])
		if err != nil {
			continue
		}

		empBirthMap[emp] = month
	}

	count := 0
	for _, m := range empBirthMap {
		if m == targetMonth {
			count++
		}
	}

	return count
}

// // countBirthdayGifts 统计指定月份需要准备的礼物数量
// func countBirthdayGifts(targetMonth int, employeeList []string, birthdayList []string) int {
// 	// 1. 创建一个 map，用于记录 员工姓名 -> 最终生日月份
// 	// 因为重名需要覆盖，map 的特性天然支持这一点
// 	userBirthMap := make(map[string]int)

// 	// 2. 遍历员工列表和生日列表
// 	for i := 0; i < len(employeeList); i++ {
// 		name := employeeList[i]
// 		dateStr := birthdayList[i]

// 		// 解析月份：形如 "2026/5/12" -> 分割后得到 ["2026", "5", "12"]
// 		dateParts := strings.Split(dateStr, "/")
// 		if len(dateParts) < 2 {
// 			continue // 鲁棒性处理：如果日期格式非法则跳过
// 		}

// 		// 将月份字符串转换为整数
// 		month, err := strconv.Atoi(dateParts[1])
// 		if err != nil {
// 			continue
// 		}

// 		// 存入 map，后录入的相同姓名会自动覆盖前面的月份
// 		userBirthMap[name] = month
// 	}

// 	// 3. 统计最终 map 中，月份等于目标月份的员工数量
// 	giftCount := 0
// 	for _, finalMonth := range userBirthMap {
// 		if finalMonth == targetMonth {
// 			giftCount++
// 		}
// 	}

// 	return giftCount
// }

func main1() {
	// --- 测试用例模拟 ---
	target := 5
	employees := []string{"Alice", "Bob", "Alice", "Tom"}
	birthdays := []string{"2026/5/10", "2026/6/20", "2026/7/15", "2026/5/01"}

	result := countBirthdayGifts(target, employees, birthdays)

	// 输出结果应为 1 (因为 Alice 的生日最终被覆盖成了 7 月，只有 Tom 是 5 月)
	fmt.Printf("%d 月需要准备的礼物数量为: %d\n", target, result)
}
