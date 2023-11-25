package main

import (
	"os"
	"bufio"
	"fmt"
)


const inputPath = "input.txt"
func main() {
	g := createGrid(inputPath)
	x,y,dir := findStartPos(g[0]),0,2
	str,steps := walkPath(x,y,dir,g)
	fmt.Println(string(str),steps)
}

//if an adjacent position isn't a space
//and isn't in the direction we just came from
//switch to corresponding direction
func changeDir(x,y,dir int, g [][]byte) (newDir int){
	if g[y-1][x] != 32 && dir != 2 {
		return 0
	} else if g[y][x+1] != 32 && dir != 3 {
		return 1
	} else if g[y+1][x] != 32 && dir != 0 {
		return 2
	} else if g[y][x-1] != 32 && dir != 1 {
		return 3
	}
	return -1
}

func findStartPos(g []byte) (x int) {
	for i := range g {
		if g[i] == 124 {
			return i
		}
	}
	return -1
}
func walkPath(x,y,dir int, g [][]byte) (seenLetters []byte,steps int) {
	for {
		switch dir {
		case 0: y -= 1
			break
		case 1: x += 1
			break
		case 2: y += 1
			break
		case 3: x -= 1
			break
		default:
			panic("Bad Dir")
		}
		steps++
		//check new position for special cases
		switch g[y][x] {
		case 124: break // |
		case 45: break  // -
		case 43: dir = changeDir(x,y,dir,g)
			break
		case 32: return //reached end of path
		default:
			seenLetters = append(seenLetters,g[y][x])
		}
	}
	return 
}
//create grid of bytes from input
func createGrid(path string)(g [][]byte) {
	file,err := os.Open(path)
	if err != nil {
		panic(err)
	}
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		g = append(g,[]byte(scanner.Text()))
	}
	return 
}