/*
Factor finder

User enters a number, and the program finds the factors of it
*/

package main

import (
        "fmt"
        "log"
)

func main() {
        var num int
        var factors []int

        fmt.Println(`Factor finder

Enter a number to find the factors of:`)

        _, err := fmt.Scan(&num)
        if err != nil { // if there is an error
                log.Fatal(err) // log it and exit
        }

        for i := 1; i <= int(num); i++ {
                if num % i == 0 {
                        factors = append(factors, i)
                }
        }

        fmt.Println(factors)
}
