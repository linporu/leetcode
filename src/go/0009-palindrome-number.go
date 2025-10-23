package leetcode

import "strconv"

func IsPalindrome1(x int) bool {
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

func IsPalindrome2(x int) bool {
	if x < 0 {
		return false
	}

	reverse := 0
	origin := x

	for origin > 0 {
		reverse = reverse*10 + origin%10 // add last digit
		origin = origin / 10             // remove last digit (simplified)
	}

	return reverse == x
}

// IsPalindrome3 - Optimized: only reverse half of the number
func IsPalindrome3(x int) bool {
	// Negative numbers and numbers ending with 0 (except 0 itself) are not palindromes
	if x < 0 || (x%10 == 0 && x != 0) {
		return false
	}

	reversedHalf := 0
	// Reverse only half of the number
	for x > reversedHalf {
		reversedHalf = reversedHalf*10 + x%10
		x = x / 10
	}

	// For even length: x == reversedHalf (e.g., 1221)
	// For odd length: x == reversedHalf/10 (e.g., 12321, middle digit doesn't matter)
	return x == reversedHalf || x == reversedHalf/10
}
