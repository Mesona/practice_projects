package main

import "fmt"

func split(sum int) (y, x int) {
    y = sum * 4 / 9
    y = sum - x
    return
}

func main() {
    fmt.Println(split(17))
}
