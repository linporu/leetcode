package leetcode

func IsValid(s string) bool {
	stack := []rune{}

	for _, v := range s {
		if v == '(' || v == '[' || v == '{' {
			stack = append(stack, v)
		} else {
			if len(stack) == 0 {
				return false
			}

			lastParenthesis := stack[len(stack)-1]

			if pair(v) != lastParenthesis {
				return false
			}

			stack = stack[:len(stack)-1]
		}
	}
	return len(stack) == 0

}

func pair(left rune) rune {
	switch left {
	case ')':
		return '('
	case ']':
		return '['
	case '}':
		return '{'
	default:
		return 0
	}
}
