package main

import "strconv"

func isPalindrome(x int) bool {
	if x < 0 {
		return false
	}

	xString := strconv.Itoa(x)
	start := 0
	end := len(xString) - 1

	for start < end {
		if xString[start] != xString[end] {
			return false
		} else {
			start += 1
			end -= 1
		}
	}
	return true
}
