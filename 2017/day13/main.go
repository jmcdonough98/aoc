package main

import (
	"fmt"
	"os"
	"bufio"
	"strings"
	"strconv"
)

const filePath = "input.txt"
const length = 85

func main(){
	firewall := parseInput()
	i := 0
	//loop forever until an attempt with delay i gets through
	for ; attemptRun(firewall,i); i++ {

	}
	fmt.Println(i)
}
func attemptRun(fw [][]int, delay int) (bool) {
	for i := delay; i < delay + len(fw); i++ {
		//skip empty columns
		if len(fw[i-delay]) == 0 {
			continue
		}
		//scanners repeat mod 2*(len - 1), so if the operation == 0, packet got caught
		if i % (2 * (len(fw[i-delay]) - 1 )) == 0 {
			return true
		}
	}
	return false
}

func parseInput() ([][]int){
	firewall := make([][]int,length)

	file,_ := os.Open(filePath)
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := strings.Split(scanner.Text(), ": ")
		index,_ := strconv.Atoi(line[0])
		depth,_ := strconv.Atoi(line[1])
		firewall[index] = make([]int, depth)
		firewall[index][0] = 1 //init security scanner
	}
	return firewall
}