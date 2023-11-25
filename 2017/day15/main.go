package main

import (
	"fmt"
)
const (
	iterations = 5000000
	factorA = 16807
	factorB = 48271
	modValue = 2147483647 //2^32 - 1
	comparisonMod = 65336 //2^16
)

func simulation(a,b int) (equal int) {
	for i := 0; i < iterations; i++ {
		a,b = genVal(a,factorA),genVal(b,factorB)
		if compareValues(a,b) {
			equal++
		}
	}
	return
}

func genVal(prevVal,factor int) (a int) {
	a = (prevVal*factor) % modValue
	if factor == factorA {
		for a % 4 != 0 {
			a = (a*factor) % modValue
		}
	} else {
		for a % 8 != 0 {
			a = (a*factor) % modValue
		}
	}
	return 
}


func compareValues(valA, valB int) (bool) {
	return (valA % 65536) == (valB % 65536)
}

func main() {
	fmt.Println(simulation(277,349))
}