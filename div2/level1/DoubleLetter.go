package main

import "fmt"

type DoubleLetter struct{}

func (self *DoubleLetter) ableToSolve(str string) string {
	s := []byte(str)

	if len(s)%2 != 0 {
		return "Impossible"
	}

	for x := 0; x < len(s); x++ {
		for i := 0; i < len(s)-1; i++ {
			j := i + 1
			if s[i] == s[j] {
				fmt.Println(string(s[i]), string(s[j]))
				fmt.Println(s[:i+1], s[j+1:])
				break
			}
		}
	}

	return "Possible"
}

func main() {
	x := DoubleLetter{}
	fmt.Println(x.ableToSolve("aabb"))
}
