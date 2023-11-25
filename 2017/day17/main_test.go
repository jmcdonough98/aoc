package main

import (
	"testing"
	"reflect"
)

func TestPuzzleInput(t *testing.T) {
	expected := 638
	lock := spinLock(3,2018) 
	for i := range lock {
		if lock[i] == 2017 {
			if lock[i+1] != expected {
				t.Errorf("Oh No! Expected: %v, Got: %v",expected,lock[i+1])
			}
		}
	}

}

func TestSpinLock(t *testing.T) {
	testValues := []struct {
		stepSize int
		length int
		outputLock []int
	}{
		{3,10,[]int{0,9,5,7,2,4,3,8,6,1}},
	}
	for _,val := range testValues {
		lock := spinLock(val.stepSize,val.length)
		if !reflect.DeepEqual(lock,val.outputLock) {
			t.Errorf("Oh No! Expected: %v, Got: %v",val,lock)
		}
	}
}

func TestUpdateLock(t *testing.T) {
	testValues := []struct{
		lock []int
		position int
		val int
		newLock []int
	}{
		{[]int{0},1,1,[]int{0,1}},
		{[]int{0,1},1,2,[]int{0,2,1}},
		{[]int{0,2,1},2,3,[]int{0,2,3,1}},
	}
	for _,val := range testValues {
		a := updateLock(val.position,val.val,val.lock)
		if !reflect.DeepEqual(a ,val.newLock) {
			t.Errorf("Oh no: Expected: %v, Got: %v ", val,a)
		}
	}
}