package main

func replaceSpace(s string) string {
	newStr := make([]byte, 0)
	for i := 0; i < len(s); i++ {
		if string(s[i]) == " " {
			newStr = append(newStr, []byte("%20")...)
		} else {
			newStr = append(newStr, s[i])

		}
	}

	return string(newStr)
}

func replaceSpace1(s string) string {
	newStr := make([]rune, 0)
	for _, char := range s {
		if string(char) == " " {
			newStr = append(newStr, []rune("%20")...)
		} else {
			newStr = append(newStr, char)

		}
	}

	return string(newStr)
}
