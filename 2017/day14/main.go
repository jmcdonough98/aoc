package main

import(
	"fmt"
	"strconv"
)
const input = "ugkiagan"

func main() {
	count := 0
	
	for i := 0; i < 128; i++ {
		rowString := input + "-" + strconv.Itoa(i)
		rowHash := knotHash(rowString)
		for i := range rowHash {
			if rowHash[i] == '1' {
				count++
			}
		}

	}
	fmt.Println(count)
}