/*
Snakes and ladders simulator

This program asks the user for a number and runs that many simulations of a game 
of snakes and ladders

It's goal is to find the average amount of moves required to win a game.
*/
package main

import (
        "fmt"
        "log"
        "math/rand"
)

func rollDice() int {
        return rand.Intn(6) + 1 // a random number between 0 and 6 (exclusive), +1
}

func main() {
        var amountOfMoves []int
        var simsToRun int

	// the ladders' start and end points
        laddersFrom := [7]int{4, 13, 33, 42, 50, 62, 74}
        laddersTo := [7]int{25, 46, 49, 63, 69, 81, 92}

	// the snakes' start and end points
        snakesFrom := [8]int{27, 40, 43, 54, 66, 76, 89, 99}
        snakesTo := [8]int{5, 3, 18, 31, 45, 58, 53, 41}

        fmt.Println(`Snakes and ladders simulator

This program attempts to find the average amount of moves required to win a game of snakes and ladders.
`)
        fmt.Println("How many simulations would you like to run?")
        _, err := fmt.Scan(&simsToRun)
        if err != nil { // if error
                log.Fatal(err) // print it and exit
        }

        totalSims := simsToRun // this will be important later

        for simsToRun > 0 {
                if (totalSims - simsToRun) % 10000 == 0 {
			// every ten thousand simulations, tell the user how many simulations have been run
                        fmt.Println(totalSims - simsToRun, "simulations run...")
                }

                simsToRun--

                movesTaken := 0
                pos := 1
                stepsToMove := 0

                for pos != 100 {
                        movesTaken++

                        stepsToMove = rollDice()

                        if stepsToMove + pos > 100 {
                                continue // can't move if it is on 97 and rolls a 5
                        }

                        pos += stepsToMove

                        for i := 0; i < len(laddersFrom); i++ {
                                if pos == laddersFrom[i] { // if on the start of a ladder
                                        pos = laddersTo[i] // go to the end
                                }
                        }

                        for i := 0; i < len(snakesFrom); i++ {
                                if pos == snakesFrom[i] { // if on a snake's head
                                        pos = snakesTo[i] // go to it's tail
                                }
                        }
                }

                amountOfMoves = append(amountOfMoves, movesTaken)
        }

        var totalMoves int = 0

        for i := 0; i < totalSims; i++ {
                totalMoves += amountOfMoves[i] // get all of the moves used across all simulations
        }

        fmt.Println("Each game took an average of", totalMoves / totalSims, "moves to win.")

        minMoves := 100000000
        maxMoves := 0
        for i := 0; i < totalSims; i++ {
                if amountOfMoves[i] < minMoves { // find the smallest number
                        minMoves = amountOfMoves[i]
                }
                if amountOfMoves[i] > maxMoves { // find the biggest number
                        maxMoves = amountOfMoves[i]
                }
        }

        fmt.Println("The most moves required was", maxMoves)
        fmt.Println("The least moves required was", minMoves)
}
