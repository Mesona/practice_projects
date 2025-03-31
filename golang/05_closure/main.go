package main

import "fmt"

func wrapper() func() int {
	x := 0
	fmt.Println("Test")
	return func() int {
		x++
		return x
	}
}

fmt.Println("test2")

func main() {
	increment := wrapper()
	fmt.Println(increment())
	fmt.Println(increment())
}
