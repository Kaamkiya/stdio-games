# stdio-games

Une collection de jeux et autres choses qui utilisent seulement la texte. 

Ils sont fait en [C++](https://devdocs.io/cpp/), [Python](https://docs.python.org/), [Go](https://go.dev/), [Ruby](https://ruby-lang.org/), et [Java](https://java.com/).

## Installation

T'a besoin de `git` pour jouer ces jeux:

```bash
$ git clone https://github.com/Kaamkiya/stdio-games.git
```

Puis `cd` à la directoire:

```bash
$ cd stdio-games/fr
```

Le `/fr` est pour aller a la dossier Français. Sinon, on jou des jeux en anglais.

## Jouer

<details>
<summary><h4>C++</h4></summary>

Pour jouer les jeux en C++, il faut `cd` à la `cpp` dossier. 

Ensuite, utilise la commande suivant[^1] pour __compiler__ un jeu:

```bash
$ g++ -o a.out <JEUX>.cpp
```

N'oublie pas de replacer `<JEUX>` avec une des jeux dans la dossier.

Pour faire jouer le jeu:

```bash
$ ./a.out
```

C'est tout!
</details>

<details>
<summary><h4>Python</h4></summary>

La premiere étape est de `cd` à la dossier:

```bash
$ cd python
```

Puis, utilise le commande `python` (ou peut-être `python3`) pour faire jouer la jeu:

```bash
$ python <JEUX>.py
```

Et voilà!
</details>

<details>
<summary><h4>Go</h4></summary>

Pour jouer les jeux en Golang, il faut `cd` à la dossier `go`. 

Puis, utilise la commande prochaine[^1] pour faire compiler un jeu:

```bash
$ go build <JEUX>.go
```

Ou `<JEUX>` est une des jeux dans la dossier.

Pour faire jouer la code compilé:

```bash
$ ./<JEUX>
```

Voilà! Simple, non?
</details>

<details>
<summary><h4>Ruby</h4></summary>

Pour jouer les jeux en Ruby, `cd` à l'interieure du dossier:

```bash
$ cd ruby
```

Ensuite, utilise la commande `ruby`[^3] pour faire jouer la jeux:

```bash
$ ruby <JEUX>.rb
```

Faites certaines a replacer `<JEUX>` avec une des jeux dans la dossier!
</details>

## À propos des jeux

Pour apprendre à propos de chaque jeu, jetez un coup d'oeuil a la (seulement un anglias pour l'instant) [wiki](https://github.com/Kaamkiya/stdio-games/wiki).

## Contribuer

J'accepte des contributions. Pour aider, vois le [documentation de contributions](.github/CONTRIBUTING.md) (seulement anglais pour maintenant).

## Notes

Il y aura beaucoup de langues de codage differents dans cet collection.

Ceci c'est une liste des langues que je ne additione pas a moi-même:

* Ruby

[^1]: tu as besoin d'installer g++ pour jouer les jeux C++
[^2]: vous avez besoin d'installer python3 pour jouer les jeux Python
[^3]: vous avez besoin d'installer ruby-full pour jouer les jeux Ruby
[^5]: vous avez besoin d'installer golang >=1.20 pour jouer les jeux Go
