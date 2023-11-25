package main

import (
	"fmt"
	"os"
	"bufio"
	"strings"
)
const path = "input.txt"

func main() {
	pipes := parseInput()
	x := countGroups(pipes) 

	
	fmt.Println(x-1)
}
func countGroups(pipes [][]string) (c int) {
	m := make(map[string]bool) 
	for i := range pipes {
		m[pipes[i][0]] = false
	}
	done := false
	for c = 0; !done ; c++ {
		done = true
		var rep string
		for i := range pipes {
			if !m[pipes[i][0]] {
				done = false
				rep = pipes[i][0]
				break
			}
		}
		tmp := countConnections(rep,pipes)
		for i := range tmp {
			if tmp[i] {
				m[i] = true
			}
		}
	}

	return c
}
func countConnections(rep string, pipes [][]string) (map[string]bool) {
	m := make(map[string]bool)
	changed := true
	for i := range pipes {
		m[pipes[i][0]] = false
	}
	m[rep] = true
	//loop through until nothing is changed
	for changed {
		changed = false
		for i := range pipes {
			for j := range pipes[i] {
				//unknown if connected
				if !m[pipes[i][0]] {
					break
				}
				//skip "<->"
				if pipes[i][j] == "<->" {
					continue
				} else if !m[pipes[i][j]]{ //if not already listed
					m[pipes[i][j]] = true
					changed = true
				}

			}
		}
	}
	//fmt.Println(m)
	return m
}

func parseInput() (pipes [][]string) {
	file,_ := os.Open(path)
	defer file.Close()
	scanner := bufio.NewScanner(file)
	//parse each line and append to array
	for scanner.Scan() {
		line := strings.Split(scanner.Text(), " ")
		for i := range line {
			line[i] = strings.Trim(line[i],",")
		}
		pipes = append(pipes,line)
		
	}
	return
}