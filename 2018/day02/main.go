package main

import (
	"bufio"
	"fmt"
	"os"
)

var path = "input.txt"

func main() {
	lines := parseInput(path)
	IDOne, IDTwo := part2(lines)
	fmt.Println("Part 1:", part1(lines), "\nPart 2:", IDOne, ",", IDTwo)
}

func part1(lines []string) int {
	two := 0
	three := 0
	for _, v := range lines {
		counts := make(map[byte]int)
		for i := range v {
			counts[v[i]]++
		}
		for i := range counts {
			if counts[i] == 2 {
				two++
				break
			}
		}
		for i := range counts {
			if counts[i] == 3 {
				three++
				break
			}
		}
	}
	return two * three
}

func part2(lines []string) (string, string) {
	for i := 0; i < len(lines); i++ {
		for j := i + 1; j < len(lines)-1; j++ {
			//fmt.Println(lines[i])
			diffCount := 0
			for k := 0; k < len(lines[i]); k++ {
				if lines[i][k] != lines[j][k] {
					if diffCount > 1 {
						break
					}
					diffCount++
				}
			}
			if diffCount == 1 {
				return lines[i], lines[j]
			}

		}
	}
	return "", ""
}

func parseInput(path string) (lines []string) {
	file, _ := os.Open(path)
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	return
}
