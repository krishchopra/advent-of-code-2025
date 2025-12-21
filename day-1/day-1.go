// attempt at using go....will circle back maybe

package main

import (
	"fmt"
	"os"
)

func main() {
	num_zeroes := 0; // var num_zeroes int = 0;
	data, _ := os.ReadFile("input.txt");
    fmt.Println(data, num_zeroes);
}
