package main

import (
	"fmt"
)

const target = 347991
const size = 1001
const half = size / 2

//dir 0 = right 1 = up 2 = left 3 = down

func main() {
	var spiral [size][size]int
	spiral[half][half] = 1

	dir := 3
	row,col := half,half
	step := 1
	found := false

	for !found {
		for i := 0; i < 2 && !found; i++ {
			dir = (dir + 1) % 4
			for j := 0; j < step ; j++ {
				col,row = moveDir(dir,row,col)
				if row >= size || dir >= size {
					found = true
					break
				}
				spiral[row][col] = sumAdj(spiral,row,col)
				if spiral[row][col] > target {
					fmt.Println(spiral[row][col])
					return
					
				}
			}
			
		}
		step++
		
	}
	//fmt.Println(spiral)

	//build array 
	//find entry
	//compute distance
}
func sumAdj(a [size][size]int, row,col int) (int) {	
	return a[row-1][col-1]+ a[row][col-1] + a[row+1][col-1] + a[row+1][col] + a[row+1][col+1] + a[row][col+1] + a[row-1][col+1] + a[row-1][col]
}

func moveDir(dir,col,row int) (x,y int) {
	switch dir {
	case 0: col++
		break
	case 1: row--
		break
	case 2: col--
		break	
	case 3: row++
		break
	}
	return row, col
}
