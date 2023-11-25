package main

import (
	"fmt"
	"time"
)
const (
	testStepSize = 3
	inputStepSize = 349
	testIter = 10
	inputIter = 50000001
)

//Part 1 Answer - Value after 2017
func findAnswer(lock []int) (int) {
	for i := range lock {
		if lock[i] == 2017 {
			return lock[i+1]
		}
	}
	return 0
}

//builds the spinlock with a given step and size
func spinLock(step,size int) ([]int) {
	position := 0
	lock := make([]int, 2)

	for i := 1; i < size; i++ {
		position = (position + step) % i + 1
		if position == 1 {
			lock[1] = i
		}
	}

	return lock
}


//insert value into lock
func updateLock(pos, i int, lock []int) ([]int) {
	tmp := make([]int, len(lock) + 1)
	for j := 0; j < pos; j++ {
		tmp[j] = lock[j]
	}
	tmp[pos] = i
	for j := pos + 1; j < len(tmp);j++ {
		tmp[j] = lock[j-1]
	}
	return tmp
}
func main() {
	t0 := time.Now()
	lock := spinLock(inputStepSize,inputIter)
	fmt.Println("Answer: ", lock[1], "\nTime: ",time.Since(t0))
}