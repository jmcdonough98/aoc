package main

import (
	"strings"
	"bufio"
	"os"
	"fmt"
)
const inputPath = "input.txt"
func main() {
	//import puzzle input into a 2d slice
	g := makeGrid(1001)
	tmp := parseInput(inputPath)
	//padding
	
	for i,j := (len(g)/2 - len(tmp)/2),0; j < len(tmp);i,j = i+1,j+1 {
		for k,l := (len(g)/2 - len(tmp)/2),0; l < len(tmp); k,l = k+1,l+1 {
			g[i][k] = tmp[j][l]
		}
	}
	count := 0
	d := 0
	x,y := len(g) / 2, len(g)/2

	for i := 0; i < 10000000; i++ {
		if g[y][x] == 0 {
			d--
			if d == -1 {
				d = 3
			}
		} else if g[y][x] == 2 {
			d = (d+1) % 4
		} else if g[y][x] == 3 {
			d = (d+2) % 4
		}
		g[y][x] = (g[y][x]+1) % 4
		if g[y][x] == 2 {
			count++
		}

		x,y = move(x,y,d)
	}
	fmt.Println(count)
}

func move(x,y,d int) (_,_ int) {
	switch d {
	case 0: y--
		break
	case 1: x++
		break
	case 2: y++
		break
	case 3: x--
		break
	default:
		panic("Unknown Direction")
	}
	return x,y
}
func parseInput(path string) (input [][]int) {
	
	file,_ := os.Open(path)
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := strings.Split(scanner.Text(),"")
		tmp := make([]int,0)
		for i := range line {
			if line[i] == "." {
				tmp = append(tmp,0)
			} else {
				tmp = append(tmp,2)
			}
		}
		input = append(input,tmp)
	}
	return 
}
func makeGrid(size int) (g [][]int) {
	g = make([][]int,size)
	for i := range g {
		g[i] = make([]int, size)
	}

	return
}