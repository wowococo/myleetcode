package main

import (
	"fmt"
	"sort"
)

func sortsssStr(s string) string {
	rStr := []rune(s)
	i, j := 0, len(rStr)-1
	for i < j {
		if rStr[i] > rStr[j] {
			rStr[i], rStr[j] = rStr[j], rStr[i]
			i++
		} else {
			i++
			j--
		}

	}

	sort.Ints(rStr)

	return string(rStr)
}

func main() {
	fmt.Println(sortStr("ate"))
	fmt.Println(sortStr("tea"))
	fmt.Println(sortStr("eat"))

}
