# stdio-games

A collection of games and animations, as well as animations, that use only the standard i/o (input/output).

They are coded in [C++](https://devdocs.io/cpp/), [Python](https://docs.python.org/), [Go](https://go.dev/), [Ruby](https://ruby-lang.org/), and [Java](https://java.com/).

## Installation

You need to have git installed to use these scripts. Run the following command to clone the repo:

```bash
$ git clone https://github.com/Kaamkiya/stdio-games.git
```

Then `cd` into the directory:

```bash
$ cd stdio-games
```

## Playing

<details>
<summary><h4>C++</h4></summary>

To play the C++ games, you have to `cd` into the `cpp` folder. 

Then, run the following command to compile[^1] a game:

```bash
$ g++ -o a.out <GAME>.cpp
```

Don't forget to replace `<GAME>` with one of the files.

To run the code, type the follwing command and hit enter:

```bash
$ ./a.out
```

This will tell the terminal/command prompt to execute the compiled code. That's it!
</details>

<details>
<summary><h4>Python</h4></summary>

The first step is to `cd` into the folder:

```bash
$ cd python
```

Then use the `python` (or maybe on your device it's `python3`) command to run the Python games:

```bash
$ python <FILE>.py
```

It should start running the code!
</details>

<details>
<summary><h4>Go</h4></summary>

To play the Golang games, you have to `cd` into the `go` directory. 

Then, run the following command to compile[^1] a game:

```bash
$ go build <GAME>.go
```

Don't forget to replace `<GAME>` with one of the files.

To run the code, type the follwing command and hit enter:

```bash
$ ./<GAME>
```

This will tell the terminal/command prompt to execute the compiled code. That's it!
</details>

<details>
<summary><h4>Ruby</h4></summary>

To run the Ruby games, `cd` into the directory:

```bash
$ cd ruby
```

Then use the `ruby` command[^3] to run the code:

```bash
$ ruby <FILE>.rb
```

Make sure to replace `<FILE>` with one of the files in the folder!
</details>

<details>
<summary><h4>Java</h4></summary>

To run the Java games, `cd` into the folder:

```bash
$ cd java
```

Then run the following command to compile[^4] the code for a file:

```bash
$ javac <FILE>.java
```

Remember to replace `<FILE>` with the name of one of the files in the directory!

To execute the compiled code, run the following command[^4]:

```bash
$ java <FILE>
```

Where `<FILE>` is the name of the file you compiled. 
</details>

## About the games

To learn about each individual game and it's purpose, visit the [wiki](https://github.com/Kaamkiya/stdio-games/wiki).

## Contributing:

I welcome contributions. If you want to help, see the [contributing docs](.github/CONTRIBUTING.md).

## Sidenotes

There will be quite a few coding languages in this repo, as I am trying out a lot and sticking with what I like.

That said, here are the languages I am not personally updating:

* Java
* Ruby

[^1]: g++ must be installed to compile C++ games
[^2]: python is needed to run the Python projects
[^3]: ruby-full is needed to run any of the Ruby games
[^4]: default-jdk is required to run and compile Java
[^5]: golang >=1.21 is required for exuction and compilation of Golang
