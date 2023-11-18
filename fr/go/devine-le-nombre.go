/*
Devine la nombre

Dans cet jeu, un nombre est choisi par hasard entre 1 et 100. Le jouer devine la nombre.
*/

package main

import (
        "fmt"
        "math/rand" // pour générer les nombres par hasard
)

func main() {
        var nombre int = rand.Intn(100) + 1 // ça c'est comment ont trouve un nombre par hasard

        fmt.Println("Je pense a un nombre entre 1 et 100.")
        fmt.Println("Pouvez-vous le deviner?")

        for { // Go n'a pas un boucle `while`, alors on utilise `for` sans parametres
                var nombreDevine int
                fmt.Scan(&nombreDevine) // ça c'est comment on prent le reponse de l'utilisateur

                if nombreDevine < nombre {
                        fmt.Println("Trop petit!")
                } else if nombreDevine > nombre {
                        fmt.Println("Trop large!")
                } else {
                        break
                }
        }

        fmt.Println("Oui, c'est la reponse!")
}
