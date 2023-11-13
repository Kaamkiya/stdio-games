/*
FizzBuzz

The user enters a number. For every number up to that number:

If the number is divisible by 3, print Fizz
If the number is divisible by 5, print Buzz
If the number is divisible by 5 and 3, print FizzBuzz
Else, print the number
*/

package main

import "fmt"

func main() {
        fmt.Println(`FizzBuzz
The classic coding challenge. 

Start at one, and go as high as the user wants. 
If the number is divisible by 3, print Fizz.
If the number is divisible by 5, print Buzz.
If the number is divisible by 3 and 5, print FizzBuzz.

Otherwise, simply print the number.`)
        var max int

        fmt.Println("How high would you like to go?")
        _, err := fmt.Scan(&max) // _, err := means catch the values this returns
        if err != nil { // if there is an error, 
                fmt.Println("\033[31;1mError") // print it
                return // and exit
        }

        for i := 1; i <= max; i++ { // := is how you let go infer types
        	// Now for actual FizzBuzz
                if i % 15 == 0 {
                        fmt.Println("FizzBuzz")
                } else if i % 3 == 0 {
                        fmt.Println("Fizz")
                } else if i % 5 == 0 {
                        fmt.Println("Buzz")
                } else {
                        fmt.Println(i)
                }
        }
}
