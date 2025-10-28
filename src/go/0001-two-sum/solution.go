package leetcode0001

func TwoSum(nums []int, target int) []int {
	dict := map[int]int{}

	for i := range nums {
		complement := target - nums[i]
		if value, exists := dict[complement]; exists {
			return []int{i, value}
		}
		dict[nums[i]] = i
	}
	return []int{}
}
