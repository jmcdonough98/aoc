package main

import (
	"fmt"
)

func main() {
	//manually convert assembly code to Go code, and optimize
	h := 0
	f := false
	for b := 109300; b <= 126300; b += 17 {
		for d := 2; d < b && !f; d++ {
			if b % d != 0 {
				continue
			}
			for e := 2; e < b && !f; e++ {
				if b % e != 0 {
					continue
				}
				if d*e == b {
					f = true	
				}
				if h > 1000 {
					fmt.Println(b,d,e,h)
					return 
				}
			}	
		}
		if f {
			h++
			f = false
		}
	}
	fmt.Println(h)
}