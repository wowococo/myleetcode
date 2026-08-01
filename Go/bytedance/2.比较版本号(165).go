package main

import (
	"fmt"
	"strconv"
	"strings"
)

// @lc code=start
// 第一种解法思路比较直接，
// 使用 strings.Split 将两个版本号按 . 切分为字符串数组，
// 然后逐个转换为整数比较。
// 时间复杂度 O（N+M）
// 空间复杂度 0（N+M）
func compareVersion(version1 string, version2 string) int {
	// 按 . 将字符串拆分为字符串切片
	part1 := strings.Split(version1, ".")
	part2 := strings.Split(version2, ".")

	m, n := len(part1), len(part2)
	// 获取最大长度，确保较短的版本号也能比完
	maxLen := m
	if n > maxLen {
		maxLen = n
	}

	// 第一种解法因为通过.拆分成数组，可以一起遍历，使用相同的 i 指针
	for i := 0; i < maxLen; i++ {
		var num1, num2 int
		// 如果没越界，就把字符串切片转成整数；越界则保持默认值 0
		if i < m {
			num1, _ = strconv.Atoi(part1[i]) // strconv.Atoi 会自动去除前导零，如 "001" -> 1
		}

		if i < n {
			num2, _ = strconv.Atoi(part2[i])
		}

		if num1 > num2 {
			return 1
		}

		if num1 < num2 {
			return -1
		}
	}

	return 0
}

// 第二种解法，双指针可以实现零内存分配
// 第二种双指针 i, j 在内部各自遍历自己的
// 时间复杂度：O(max(N,M))  --- 最多遍历较长的字符串一次
// 空间复杂度：O(1) - 仅使用常数级别的额外空间
func compareVersion2(version1 string, version2 string) int {
	m, n := len(version1), len(version2)
	i, j := 0, 0

	// 只要有一个字符串还没遍历完，就继续比较
	for i < m || j < n {
		var num1, num2 int

		for i < m && version1[i] != '.' {
			num1 = num1*10 + int(version1[i]-'0')
			i++
		}

		for j < n && version2[j] != '.' {
			num2 = num2*10 + int(version2[j]-'0')
			j++
		}

		if num1 > num2 {
			return 1
		}

		if num1 < num2 {
			return -1
		}

		// 跳过 '.'
		i++
		j++
	}

	return 0
}

func main2() {
	// 测试用例
	fmt.Println(compareVersion("0.1", "1.1"))       // 输出 -1
	fmt.Println(compareVersion("1.0.1", "1"))       // 输出 1
	fmt.Println(compareVersion("7.5.2.4", "7.5.3")) // 输出 -1
	fmt.Println(compareVersion("1.01", "1.001"))    // 输出 0
	fmt.Println(compareVersion("1.0", "1.0.0"))     // 输出 0

	fmt.Println(compareVersion2("0.1", "1.1"))       // 输出 -1
	fmt.Println(compareVersion2("1.0.1", "1"))       // 输出 1
	fmt.Println(compareVersion2("7.5.2.4", "7.5.3")) // 输出 -1
	fmt.Println(compareVersion2("1.01", "1.001"))    // 输出 0
	fmt.Println(compareVersion2("1.0", "1.0.0"))     // 输出 0
}

/*
num1 = num1*10 + int(version1[i]-'0')
绝对不需要死记硬背！这行代码在算法面试和底层开发中非常高频，把它拆成**两个基础概念**理解后，以后想忘都难：

---

### 第一步：`version1[i] - '0'`（把字符转成对应的数字）

在 Go 语言中，从字符串里按索引取出的 `version1[i]` 不是数字，而是一个 **ASCII 字符（byte/uint8 类型）**。

在 ASCII 编码表里，数字字符 `'0'` 到 `'9'` 是**连续排列**的：

* 字符 `'0'` 的 ASCII 码值是 `48`
* 字符 `'1'` 的 ASCII 码值是 `49`
* 字符 `'5'` 的 ASCII 码值是 `53`

因为它们是连续的，所以**用任何数字字符减去 `'0'`，结果刚好就是它对应的实际整数值**：

* `'0' - '0'` $\rightarrow$ `48 - 48 = 0`
* `'5' - '0'` $\rightarrow$ `53 - 48 = 5`
* `'9' - '0'` $\rightarrow$ `57 - 48 = 9`

外层的 `int(...)` 只是把计算得到的 `byte` 强制转换成 `int` 类型，方便后续计算。

---

### 第二步：`num1 = num1 * 10 + ...`（从左到右按十进制拼接多位数）

这是用代码**从左往右构建多位数**的标准写法。

我们平时写十进制数字，比如 `123`，它的本质是：$1 \times 100 + 2 \times 10 + 3$。

但程序在遍历字符串 `"123"` 时，是一步一步从左往右读的：

| 步骤 | 读到的字符 | 计算过程 | `num1` 的最新值 |
| --- | --- | --- | --- |
| **初始** | - | - | `0` |
| **第 1 次** | `'1'`（数字 1） | `num1 = 0 * 10 + 1` | **`1`** |
| **第 2 次** | `'2'`（数字 2） | `num1 = 1 * 10 + 2` | **`12`**（把原来的 `1` 往左退一位，给 `2` 腾出个位） |
| **第 3 次** | `'3'`（数字 3） | `num1 = 12 * 10 + 3` | **`123`**（把原来的 `12` 往左退一位，给 `3` 腾出个位） |

每读一个新数字，就把前面的累加结果**乘以 10（相当于整体左移一位）**，再加上新的个位数。

---

### 面试官为什么喜欢看你这么写？

调用官方库 `strconv.Atoi("123")` 固然简单，但它内部其实也是用这个原理实现的。

手动写出这行代码，能向面试官传递两个信号：

1. **理解底层编码**：你知道字符 `'5'` 和数字 `5` 在内存里的区别（ASCII 码）。
2. **注重极致性能**：避免了字符串切片和内置函数调用的额外开销，实现了 $O(1)$ 零内存分配。

*/
