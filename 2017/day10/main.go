package main

import (
	"encoding/hex"
)
const listSize = 256
//const input = "192,69,168,160,78,1,166,28,0,83,198,2,254,255,41,12"

func main() {
	//convert string input into slice of bytes

	// lengths := []byte(input)
	// lengths = append(lengths,  []byte{17,31,73,47,23}...)
	
	//make a slice of integers from 0 to 255
	// list := make([]int,listSize)
	// for i := range list {
	// 	list[i] = i
	// }

	//sparse hash
	//sparseHash(list,lengths)

	//reduce to dense hash
	//dense := denseHash(list)
	
	//encode and display as hexadecimal
	//fmt.Println(hex.EncodeToString(dense),"\nTime: ",time.Since(t0))
} 

func knotHash(in string) (hash string) {

	//convert string input into slice of bytes
	lengths := []byte(in)
	lengths = append(lengths,  []byte{17,31,73,47,23}...)

	//make a slice of integers from 0 to 255
	list := make([]int,listSize)
	for i := range list {
		list[i] = i
	}

	//sparse hash
	sparseHash(list,lengths)

	//reduce to dense hash
	dense := denseHash(list)

	return hex.EncodeToString(dense)
}

func sparseHash(list []int, lengths []byte)  {
	position,step := 0,0
	for j := 0; j < 64; j++ {
		for i := range lengths {
			reverse(list,position,int(lengths[i]))
			position = (position + int(lengths[i])+step) % len(list)
			step++
		}
	}
}

func denseHash(list []int)([]byte) {
	dense := make([]byte,16)
	for i := 0; i < 16; i++ {
		block := list[16*i:16*(i+1)]
		//xor together each block
		for j := range block{
			dense[i] ^= byte(block[j])
		}
	}
	return dense
}
//reversing function that allows for wrapping around the slice
func reverse(a []int, start, length int) {
	b := make([]int, length)
	for i := 0; i < length; i++ {
		b[i] = a[(start + i) % len(a)]
	}
	for i := 0; i < len(b)/2;i++ {
		b[i],b[len(b)- i-1] = b[len(b) - i-1],b[i]
	}
	for i := 0; i < length; i++ {
		a[(start + i) % len(a)] = b[i]
	}
} 