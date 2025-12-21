package main

import (
	"bufio"
	"fmt"
	"log"
	"math"
	"os"
)

func calculateLargestJoltage(joltages []int) int {
	// iterate and find largest int until last element
	first, firstIdx := joltages[0], 0
	for i := 0; i < len(joltages)-1; i++ {
		if joltages[i] > first {
			first = joltages[i]
			firstIdx = i
		}
	}
	second := joltages[firstIdx+1]
	for j := firstIdx + 1; j < len(joltages); j++ {
		if joltages[j] > second {
			second = joltages[j]
		}
	}
	return 10 * first + second
}

func calculateLargestJoltageGeneric(joltages []int, n int, used []int) int {
	// base case
	if n == 0 {
		total, powerOf10 := 0, 0
		for i := len(used) - 1; i >= 0; i-- {
			total += (used[i] * int(math.Pow(10, float64(powerOf10))))
			powerOf10++
		}
		return total
	}
	// iterate and find largest int until last element
	highest, index := joltages[0], 0
	for i := 0; i < len(joltages)-n+1; i++ {
		if joltages[i] > highest {
			highest = joltages[i]
			index = i
		}
	}
	used = append(used, highest)
	return calculateLargestJoltageGeneric(joltages[index+1:], n-1, used)
}

func part1() {
    file, err := os.Open("data.txt")
    if err != nil {
        log.Fatal(err)
    }
    defer file.Close()
    scanner := bufio.NewScanner(file)

    // actual logic
	sumJoltages := 0

    for scanner.Scan() {
        joltagesString := scanner.Text()
		joltages := []int{}
		for _, char := range joltagesString {
			joltages = append(joltages, int(char-'0'))
		}
		sumJoltages += calculateLargestJoltageGeneric(joltages, 12, []int{})
	}
	fmt.Printf("Sum of largest joltages: %d\n", sumJoltages)
}


func main() {
    part1()
}
