package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func mod(a, b int) int {
    return (a % b + b) % b
}

func part1() {
    file, err := os.Open("data.txt")
    if err != nil {
        log.Fatal(err)
    }
    defer file.Close()
    scanner := bufio.NewScanner(file)

    // actual logic
    position, password := 50, 0

    for scanner.Scan() {
        change := scanner.Text()
        delta, err := strconv.Atoi(change[1:])
        if err != nil {
            log.Fatal(err)
        }
        if (change[0] == 'L') {
            position = mod(position - delta, 100)
        } else {
            position = mod(position + delta, 100)
        }
        if (position == 0) {
            password += 1
        }
    }

    if err := scanner.Err(); err != nil {
        log.Fatal(err)
    }

    fmt.Printf("Final Position: %d, Password: %d\n", position, password)
}

func part2() {
    file, err := os.Open("data.txt")
    if err != nil {
        log.Fatal(err)
    }
    defer file.Close()
    scanner := bufio.NewScanner(file)

    // actual logic
    position, password := 50, 0

    for scanner.Scan() {
        change := scanner.Text()
        delta, err := strconv.Atoi(change[1:])
        if err != nil {
            log.Fatal(err)
        }
        // multiple rotations required
        if (delta > 100) {
            rotations, remainder := delta / 100, delta % 100
            password += rotations
            delta = remainder
        }
        if (change[0] == 'L') {
            if (position > 0 && position - delta <= 0) {
                password += 1
            }
            position = mod(position - delta, 100)
        } else {
            if (position < 100 && position + delta >= 100) {
                password += 1
            }
            position = mod(position + delta, 100)
        }

    }

    if err := scanner.Err(); err != nil {
        log.Fatal(err)
    }

    fmt.Printf("Final Position: %d, Password: %d\n", position, password)
}

func main() {
    part2()
}
