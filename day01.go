package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"unicode"
	"unicode/utf8"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func getFirstDigit(line string) string {
	for _, runeValue := range line {
		if unicode.IsDigit(runeValue) {
			return string(runeValue)
		}
	}
	return ""
}

func getLastDigit(line string) string {
	for i := len(line) - 1; i >= 0; i-- {
		runeValue, _ := utf8.DecodeRuneInString(line[i:])
		if unicode.IsDigit(runeValue) {
			return string(runeValue)
		}
	}

	return ""
}
func main() {
	file, err := os.Open("day01.txt")
	check(err)
	defer file.Close()
	scanner := bufio.NewScanner(file)
	total := 0
	for scanner.Scan() {
		num, err := strconv.Atoi(getFirstDigit(scanner.Text()) + getLastDigit(scanner.Text()))
		check(err)

		total += num
	}
	fmt.Println(total)

}
