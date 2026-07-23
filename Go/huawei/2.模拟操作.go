package main

import (
	"fmt"
	"strconv"
	"strings"
)

type Command struct {
	Opt       string // add_rule, mod_rule, del_rule
	RuleID    int    // -1 表示未提供
	RuleIndex int    //-1 表示未提供
	Valid     bool   //格式与范围是否合法
}

func parseCommand(line string) Command {
	parts := strings.Fields(line)
	if len(parts) == 0 {
		return Command{Valid: false}
	}

	cmd := Command{
		Opt:       parts[0],
		RuleID:    -1,
		RuleIndex: -1,
		Valid:     true,
	}

	// 校验操作关键字
	if cmd.Opt != "add_rule" && cmd.Opt != "mod_rule" && cmd.Opt != "del_rule" {
		cmd.Valid = false
		return cmd
	}

	for _, part := range parts[1:] {
		kv := strings.Split(part, "=")
		if len(kv) != 2 {
			cmd.Valid = false
			return cmd
		}

		key, valStr := kv[0], kv[1]
		val, err := strconv.Atoi(valStr)
		if err != nil || (val < 1 || val > 9999) {
			cmd.Valid = false
			return cmd
		}
		if key == "rule_id" {
			cmd.RuleID = val
		} else if key == "rule_index" {
			cmd.RuleIndex = val
		}
	}

	// 根据不同操作校验必要参数是否存在
	switch cmd.Opt {
	case "add_rule", "mod_rule":
		// 添加和修改必须同时包含 rule_id 和 rule_index
		if cmd.RuleID == -1 || cmd.RuleIndex == -1 {
			cmd.Valid = false
		}
	case "del_rule":
		// 删除操作必须包含 rule_id
		if cmd.RuleID == -1 {
			cmd.Valid = false
		}
	}
	return cmd
}

func processCommand(ruleMap map[int]int, line string) string {
	cmd := parseCommand(line)
	if !cmd.Valid {
		return "failure"
	}

	switch cmd.Opt {
	case "add_rule":
		if _, exist := ruleMap[cmd.RuleID]; exist {
			return "failure"
		}

		ruleMap[cmd.RuleID] = cmd.RuleIndex
		return "success"

	case "mod_rule":
		if oldIndex, exist := ruleMap[cmd.RuleID]; !exist || oldIndex == cmd.RuleIndex {
			return "failure"
		}

		ruleMap[cmd.RuleID] = cmd.RuleIndex
		return "success"
	case "del_rule":
		if _, exist := ruleMap[cmd.RuleID]; !exist {
			return "failure"
		}

		delete(ruleMap, cmd.RuleID)
		return "success"
	}

	return "failure"
}

// parseCommand 解析命令行字符串
func parseCommand1(line string) Command {
	parts := strings.Fields(line)
	if len(parts) == 0 {
		return Command{Valid: false}
	}

	cmd := Command{
		Opt:       parts[0],
		RuleID:    -1,
		RuleIndex: -1,
		Valid:     true,
	}

	// 校验操作关键字
	if cmd.Opt != "add_rule" && cmd.Opt != "mod_rule" && cmd.Opt != "del_rule" {
		cmd.Valid = false
		return cmd
	}

	// 解析后面的参数（考虑参数顺序可能颠倒的情况）
	for _, part := range parts[1:] {
		kv := strings.Split(part, "=")
		if len(kv) != 2 {
			cmd.Valid = false
			return cmd
		}

		key, valStr := kv[0], kv[1]
		val, err := strconv.Atoi(valStr)
		if err != nil || val < 1 || val > 9999 { // 规则：取值范围为数字 1-9999
			cmd.Valid = false
			return cmd
		}

		if key == "rule_id" {
			cmd.RuleID = val
		} else if key == "rule_index" {
			cmd.RuleIndex = val
		}
	}

	// 根据不同操作校验必要参数是否存在
	switch cmd.Opt {
	case "add_rule", "mod_rule":
		// 添加和修改必须同时包含 rule_id 和 rule_index
		if cmd.RuleID == -1 || cmd.RuleIndex == -1 {
			cmd.Valid = false
		}
	case "del_rule":
		// 删除操作必须包含 rule_id
		if cmd.RuleID == -1 {
			cmd.Valid = false
		}
	}

	return cmd
}

// ProcessCommand 执行单条指令并返回操作结果
func ProcessCommand1(rules map[int]int, line string) string {
	cmd := parseCommand1(line)

	// 1. 格式不合规、缺少关键字或数值超限 -> 失败
	if !cmd.Valid {
		return "failed"
	}

	switch cmd.Opt {
	case "add_rule":
		// 添加：必须不存在该 rule_id
		if _, exists := rules[cmd.RuleID]; exists {
			return "failed"
		}
		rules[cmd.RuleID] = cmd.RuleIndex
		return "success"

	case "mod_rule":
		// 修改：必须存在该 rule_id，且新旧 rule_index 不能完全一致
		oldIndex, exists := rules[cmd.RuleID]
		if !exists || oldIndex == cmd.RuleIndex {
			return "failed"
		}
		rules[cmd.RuleID] = cmd.RuleIndex
		return "success"

	case "del_rule":
		// 删除：必须存在该 rule_id
		if _, exists := rules[cmd.RuleID]; !exists {
			return "failed"
		}
		delete(rules, cmd.RuleID)
		return "success"
	}

	return "failed"
}

func main() {
	// 用 map 维护当前系统的规则状态 (rule_id -> rule_index)
	rules := make(map[int]int)

	// 模拟测试指令列表
	testInputs := []string{
		"add_rule rule_id=1 rule_index=18",    // 成功：添加 id=1, index=18
		"add_rule rule_id=1 rule_index=20",    // 失败：id=1 已存在
		"mod_rule rule_id=1 rule_index=100",   // 成功：修改 id=1 为 index=100
		"mod_rule rule_id=1 rule_index=100",   // 失败：前后 index 一模一样
		"mod_rule rule_id=2 rule_index=50",    // 失败：id=2 不存在
		"del_rule rule_id=1",                  // 成功：删除 id=1
		"del_rule rule_id=1",                  // 失败：id=1 已不存在
		"add_rule rule_id=10000 rule_index=5", // 失败：rule_id 超出 1-9999 范围
		"add_rule rule_id=2",                  // 失败：缺少 rule_index 属性
	}

	fmt.Println("--- 模拟指令运行结果 ---")
	for _, input := range testInputs {
		res := processCommand(rules, input)
		fmt.Printf("输入: %-36s => 输出: %s\n", input, res)
	}

	// 支持控制台实时交互输入（按 Ctrl+C 退出）
	// `fmt.Println("\n--- 请在下方输入你的指令进行测试 ---")
	// scanner := bufio.NewScanner(os.Stdin)
	// for scanner.Scan() {
	// 	line := scanner.Text()
	// 	if strings.TrimSpace(line) == "" {
	// 		continue
	// 	}
	// 	res := processCommand(rules, line)
	// 	fmt.Println(res)
	// }`
}
