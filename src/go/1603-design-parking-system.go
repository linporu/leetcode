package leetcode

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * obj := Constructor(big, medium, small);
 * param_1 := obj.AddCar(carType);
 */

// Solution 1: Map-based (cleaner code, slightly slower)
type ParkingSystem struct {
	slots map[int]int
}

func Constructor(big int, medium int, small int) ParkingSystem {
	return ParkingSystem{
		slots: map[int]int{1: big, 2: medium, 3: small},
	}
}

func (this *ParkingSystem) AddCar(carType int) bool {
	if this.slots[carType] > 0 {
		this.slots[carType] -= 1
		return true
	}
	return false
}

// Solution 2: Struct-based (faster, more verbose)
type ParkingSystem2 struct {
	big, medium, small int
}

func Constructor2(big int, medium int, small int) ParkingSystem2 {
	return ParkingSystem2{
		big:    big,
		medium: medium,
		small:  small,
	}
}

func (this *ParkingSystem2) AddCar2(carType int) bool {
	switch carType {
	case 1:
		if this.big > 0 {
			this.big--
			return true
		}
	case 2:
		if this.medium > 0 {
			this.medium--
			return true
		}
	case 3:
		if this.small > 0 {
			this.small--
			return true
		}
	}
	return false
}
