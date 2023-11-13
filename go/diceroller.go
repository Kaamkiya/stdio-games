package main

import (
        "fmt"
        "log"
        "math/rand" // for random numbers
)

func main() {
        fmt.Println(`Dice roller

In this game, I roll as many dice as you want with as many sides as you want.`)

	// declare the variables
        var amount int
        var sides int
        var total int

        fmt.Println("How many dice would you like to roll?")
        _, err := fmt.Scan(&amount)
        if err != nil {
                log.Fatal("Invalid input.")
        }

        fmt.Println("How many sides should the dice have?")
        _, err = fmt.Scan(&sides)
        if err != nil {
                log.Fatal("Invalid input.")
        }

        for i := 0; i < amount; i++ {
                total += rand.Intn(sides) + 1 // add to total
        }

        fmt.Println("The total is", total)
}
