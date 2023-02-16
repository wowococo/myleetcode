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

func replaceSpace2(s string) string {
	length := len(s)
	spaceNum := 0
	for _, char := range s {
		if char == ' ' {
			spaceNum++
		}
	}

	byteStr := []byte(s)
	temp := make([]byte, spaceNum*2)
	byteStr = append(byteStr, temp...)

	i := length - 1
	j := len(byteStr) - 1

	for i >= 0 {
		if s[i] == ' ' {
			byteStr[j] = '0'
			byteStr[j-1] = '2'
			byteStr[j-2] = '%'
			j = j - 3
			i = i - 1
		} else {
			byteStr[j] = s[i]
			j -= 1
			i -= 1
		}
	}

	return string(byteStr)

}
