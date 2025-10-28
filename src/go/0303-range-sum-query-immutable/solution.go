package leetcode0303

/**
 * Your NumArray object will be instantiated and called as such:
 * obj := Constructor(nums);
 * param_1 := obj.SumRange(left,right);
 */

// Solution 1: for loop
type NumArray struct {
	nums []int
}

func Constructor(nums []int) NumArray {
	return NumArray{
		nums: nums,
	}
}

func (this *NumArray) SumRange(left int, right int) int {
	var sum int
	for i := left; i <= right; i++ {
		sum += this.nums[i]
	}
	return sum
}

// Solution 2: prefix sum
type NumArray2 struct {
	nums []int
	sums []int
}

func Constructor2(nums []int) NumArray2 {
	if nums == nil {
		return NumArray2{
			nums: nil,
			sums: nil,
		}
	}

	sums := make([]int, len(nums))
	sums[0] = nums[0]

	for i := 1; i < len(nums); i++ {
		sums[i] = sums[i-1] + nums[i]
	}

	return NumArray2{
		nums: nums,
		sums: sums,
	}
}

func (this *NumArray2) SumRange(left int, right int) int {
	if this.sums == nil {
		return 0
	}

	if left == 0 {
		return this.sums[right]
	}
	return this.sums[right] - this.sums[left-1]
}
