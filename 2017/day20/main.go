package main

import (
	"fmt"
	"os"
	"bufio"
	"strings"
	"strconv"
)

type vector struct {
	x int
	y int
	z int
}

type particle struct {
	pos vector
	vel vector
	acc vector
	col bool
}

func step(p *particle) {
	p.vel.x += p.acc.x
	p.vel.y += p.acc.y
	p.vel.z += p.acc.z
	p.pos.x += p.vel.x
	p.pos.y += p.vel.y
	p.pos.z += p.vel.z
}
func parseVector(input string) (v vector) {
	input = strings.TrimRight(strings.TrimLeft(input,"<"),">")
	split := strings.Split(input,",")
	v.x,_ = strconv.Atoi(split[0])
	v.y,_ = strconv.Atoi(split[1])
	v.z,_ = strconv.Atoi(split[2])
	return
}
func parseInput() (particles []particle) {
	file,_ := os.Open("input.txt")
	scanner := bufio.NewScanner(file)
	
	for scanner.Scan(){
		line := scanner.Text()
		split := strings.Split(line, ", ")
		pos,vel,acc := parseVector(split[0][2:]),parseVector(split[1][2:]),parseVector(split[2][2:])
		particles = append(particles, particle{pos,vel,acc,false})
		
	}
	return
}

func simulateParticles(particles []particle) (partsLeft int) {
	checkCollisions(particles)
	for i := 0; i < 500; i++ {
		for i := range particles {
			step(&particles[i])
		}
		checkCollisions(particles)
	}
	for i := range particles {
		if !particles[i].col {
			partsLeft++
		}
	}
	return
}
func checkCollisions(particles []particle) {
	for i := 0; i < len(particles); i++ {
		if particles[i].col {
			continue
		} 
		for j := 0; j < len(particles);j++ {
			if particles[j].col {
				continue
			}
			if i != j && colliding(particles[i],particles[j]) {
				particles[i].col = true
				particles[j].col = true
			}
		}
	}
}
func colliding(a,b particle) (bool) {
	if a.pos.x == b.pos.x && a.pos.y == b.pos.y && a.pos.z == b.pos.z {
		return true
	}
	return false
}
func main() {
	particles := parseInput()
	x := simulateParticles(particles)
	fmt.Println(x)
}