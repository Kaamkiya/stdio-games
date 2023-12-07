#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int main() {
  srand((unsigned) time(NULL));
  int number = rand() % 100;
  printf("I am thinking of a number between 1 and 100. Can you guess it?\n");
  int guess = -1;
  while (guess != number) {
    scanf("%d", &guess);
    if (guess < number) {
      printf("Too small!");
    } else if (guess > number) {
      printf("Too big!");
    }
  }
  printf("Correct!");
}
