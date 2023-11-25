package main

import (
	"fmt"
	"strings"
	"os"
	"bufio"
	"sort"
)


func main(){
	file,_ := os.Open("pass.txt")
	scanner := bufio.NewScanner(file)
	count := 0
	for scanner.Scan() {
		valid := true
		m := make(map[string]int) 
		s := strings.Split(scanner.Text(), " ")
		for i := range s {
			tmp := strings.Split(s[i], "")
			sort.Strings(tmp)
			a := strings.Join(tmp,"")
			m[a]++
		}
		for i := range m {
			if m[i] > 1 {
				valid = false
			}
		}
		if valid {
			count++
		}
	}
	fmt.Println(count)
}