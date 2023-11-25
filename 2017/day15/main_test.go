package main

import "testing"

func TestSim(t *testing.T) {
	res := simulation(65,8921)
	if res != 588 {
		t.Errorf("Incorrect Simulation. Expected: %d, Actual: %d",588,res)
	}
}
func TestCompare(t *testing.T) {
	tables := []struct{
		valA int
		valB int
		equal bool
	}{
		{1092455,430625591,false},
		{1181022009,1233683848,false},
		{245556042,1431495498,true},
		{1744312007,137874439,false},
		{1352636452,285222916,false},
	}
	for _,i := range tables {
		eq := compareValues(i.valA,i.valB)
		if eq != i.equal {
			t.Errorf("Incorrect Comparison. A: %d, B: %d, Expected: %v Actual: %v", i.valA,i.valB,i.equal,eq)
		}
	}
}
func TestGenVal(t *testing.T) {
	tables := []struct{
		prevVal int
		factor int
		result int
	}{
		{65,factorA,1352636452},
		{8921,factorB,1233683848},
		// {65,16807,1092455},
		// {1092455,16807,1181022009},
		// {1181022009,16807,245556042},
		// {8921,factorB,430625591},
		// {1431495498,factorB,137874439},
	}
	for _, table := range tables {
		val := genVal(table.prevVal,table.factor)
		if val != table.result {
			t.Errorf("Incorrect Gen value for %d, factor %d. Got: %d, expected :%d",table.prevVal,table.factor,val,table.result)
		}
	}
}