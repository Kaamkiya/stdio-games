package main

import (
	"fmt"
	"log"
)

func main() {
        fmt.Println(`Collatz sequence
The collatz sequence is a series of numbers starting at n.
The next number is decided based on one of the 3 rules:

1. If n is even, the next number is n / 2
2. If n is odd, the next number is 3n + 1
3. If n is 1, terminate.

It is generallly thought, although not proven, that every number eventually terminates at 1.
        `)

        var n int
        fmt.Println("Enter a number to test this with:")
	_, err := fmt.Scan(&n)
	if err != nil {
		log.Fatal(err) // print the error if there is one
	}

        for { // go's equivalent of a while(true) loop
                fmt.Println(n)
                if n == 1 {
                        break
                }

                if n % 2 == 0 {
                        n = n / 2
                } else {
                        n = 3 * n + 1
                }
        }

}
