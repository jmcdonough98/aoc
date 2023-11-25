package main

import (
	"fmt"
	"bufio"
	"os"
	"strings"
)

func main(){
	file,_ := os.Open("in.txt")
	scanner := bufio.NewScanner(file)
	var list [][]string
	for scanner.Scan() {
		str := strings.Split(scanner.Text(), " ")
		for i := range str {
			str[i] = strings.TrimRight(str[i],",")
		}
		list = append(list,str)
		
	}
	val := list[0][0]
	for i := 0; i < len(list); i++ {
		for j := 1; j < len(list[i]); j++ {
			if val == list[i][j] {
				val = list[i][0]
				i = 0
				break
			}
		}
	}

	fmt.Println(val)

}
