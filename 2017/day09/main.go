package main

import (
	"fmt"
	"io/ioutil"
)
//iterate through characters
	//if = {
		//increment level
	//if = <
		//trash flag = true
	//if = !
		//skip next character
	//if >
		//trash flag = false
	// if  }
		//add level to score
		//decement level


func main() {
	test,_ := ioutil.ReadFile("in.txt")
	//fmt.Println(string(test))
	trash := false
	score := 0
	for i := 0; i < len(test); i++ {
		char := string(test[i])
		if char == ">" {
			trash = false
			continue
		}
		if char == "<" && !trash{
			trash = true
			continue
		}
		if char == "!" {
			i++
			continue
		}
		if trash && (char != "!"){
			fmt.Println(char,trash)
			score++
		}
		
	}
	fmt.Println(score)
}