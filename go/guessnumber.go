/*
Guess the number

In this game, a number is chosen between 1 and 100. The user guesses the number.
*/

package main

import (
        "fmt"
        "math/rand"
)

func main() {
        var number int = rand.Intn(100) + 1 // random number between 1 and 100

        fmt.Println("I am thinking of a number between 1 and 100.")
        fmt.Println("Can you guess it?")

        for { // go doesn't have a while loop, so we use `for` instead
                var guess int
                fmt.Scan(&guess) // this is how you take input in golang

                if guess < number {
                        fmt.Println("Too small!")
                } else if guess > number {
                        fmt.Println("Too big!")
                } else {
                        break
                }
        }

        fmt.Println("Correct!")
}
