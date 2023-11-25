package main

import (
	"fmt"
	"os"
	"bufio"
	"strconv"
)

func main(){
	//get path
	f,_ := os.Open("path.txt")
	scanner := bufio.NewScanner(f)
	path := make([]int,0)
	for scanner.Scan() {
		tmp := scanner.Text()
		num,_ := strconv.Atoi(tmp)
		path = append(path,num)
	}
	
	fmt.Println(followPath(path))
	// a := []int{0,3,0,1,-3}
	// fmt.Println(followPath(a))
}

func followPath(path []int)(steps int) {
	for i := 0;i < len(path); {	
		//updates offset
		if path[i] > 3 {
			path[i]--
		} else {
			path[i]++
		}
		//moves
		i += path[i] - 1
		steps++
	}
	return
}