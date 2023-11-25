package main

import (
	"fmt"
)
const (
	tapeSize = 100000
	iter     = 12964419
)
func main() {
	tape := make([]int, tapeSize)
	state := "A"
	pos := tapeSize / 2
	for i := 0; i < iter; i++ {
		switch state {
		case "A":
			if tape[pos] == 0 {
				tape[pos] = 1
				pos++
				state = "B"

			} else {
				tape[pos] = 0 
				pos++
				state = "F"
			}
			break
		case "B":
			if tape[pos] == 0 {
				tape[pos] = 0 
				pos--
				state = "B"
			} else {
				tape[pos] = 1
				pos--
				state = "C"
			}
			break
		case "C":
			if tape[pos] == 0 {
				tape[pos] = 1
				pos--
				state = "D"
			} else {
				tape[pos] = 0
				pos++
				state = "C"
			}
			break
		case "D":
			if tape[pos] == 0 {
				tape[pos] = 1
				pos--
				state = "E"
			} else {
				tape[pos] = 1
				pos++
				state = "A"
			}
			break
		case "E":
			if tape[pos] == 0 {
				tape[pos] = 1
				pos--
				state = "F"
			} else {
				tape[pos] = 0
				pos--
				state = "D"
			}
			break
		case "F":
			if tape[pos] == 0 {
				tape[pos] = 1
				pos++
				state = "A"
			} else {
				tape[pos] = 0
				pos--
				state = "E"
			}
			break
		default:
			panic("Error: Unknown State")
		}
	}
	fmt.Println(checkSum(tape))
}
func checkSum(t []int) (s int){
	for i := range t {
		if t[i] == 1 {
			s++
		}
	}
	return
}