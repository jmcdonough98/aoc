package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var path = "input.txt"

func main() {
	fmt.Println("Part 1:", partOne(path), "\nPart 2:", partTwo(path))
}

func partOne(path string) (freq int) {
	file, _ := os.Open(path)
	scan := bufio.NewScanner(file)
	for scan.Scan() {
		n, _ := strconv.Atoi(scan.Text())
		freq += n
	}
	return
}
func partTwo(path string) int {
	freq := 0
	//indices are frequencies we've seen
	freqMap := make(map[int]bool)
	freqMap[freq] = true
	for {
		file, _ := os.Open("input.txt")
		scan := bufio.NewScanner(file)
		for scan.Scan() {
			n, _ := strconv.Atoi(scan.Text())
			freq += n
			//if it's been seen, this is the second occurence
			if freqMap[freq] {
				return freq
			}
			freqMap[freq] = true
		}
	}
}
