package main

import (
	"fmt"
	"os"
	"bufio"
	"strings"
	"strconv"
)

const inputPath = "input.txt"

type instruction struct{
	op string
	reg string
	val string
}
func main() {
	ins,reg := parseInstructions(inputPath)
	sound := execInstructions(ins,reg)
	fmt.Println(reg,sound)
}

func convert(value string, reg map[string]int) (int) {
	numVal,err := strconv.Atoi(value)
	if err != nil {
		return reg[value] //value is another register
	} else {
		return numVal
	}
}

func execInstructions(ins []instruction, reg map[string]int) (lastSound int) {
	sound := 0
	for i := 0; i < len(ins);i++ {
		switch ins[i].op {
		case "snd":
			sound = reg[ins[i].reg]
			break
		case "set":
			reg[ins[i].reg] = convert(ins[i].val,reg)
			break
		case "add":
			reg[ins[i].reg] += convert(ins[i].val,reg)
			break
		case "mul":
			reg[ins[i].reg] *= convert(ins[i].val,reg)
			break
		case "mod":
			reg[ins[i].reg] %= convert(ins[i].val,reg)
			break
		case "rcv":
			if convert(ins[i].reg,reg) != 0 { return sound }
			break
		case "jgz":
			tmp := convert(ins[i].reg,reg)
			if tmp > 0 {
				//-1 to counter the loop increment
				i += ( convert(ins[i].val,reg) -1)
			}
			break
		default:
			panic("Command: not found")
		}
	}
	return
}

func parseInstructions(path string)(ins []instruction, reg map[string]int){
	file,_ := os.Open(path) 
	defer file.Close()
	scanner := bufio.NewScanner(file)
	reg = make(map[string]int) 

	for scanner.Scan() {
		parts := strings.Split(scanner.Text(), " ")
		if len(parts) == 3 {
			ins = append(ins, instruction{parts[0],parts[1], parts[2]})
		} else {
			ins = append(ins, instruction{parts[0],parts[1], ""})
		}
	}
	for i := range ins {
		if ins[i].op != "jgz" {
			reg[ins[i].reg] = 0
		}
	}
	return
}
