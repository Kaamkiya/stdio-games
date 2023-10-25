#include <iostream>

int main() {
  int number = 1 + (rand() % 100);
  
  std::cout << "I'm thinking of a number between 1 and 100. " << std::endl;
  std::cout << "Can you guess it?" << std::endl;
  
  int guess = 9991;
  
  while (guess != number) {
    std::cout << "Enter your guess: ";
    std::cin >> guess;
    
    if (guess < number) {
      std::cout << "That number is too small, try again\n";
    } else if (guess > number) {
      std::cout << "That number is too big, try again\n";
    }
  }
  
  printf("Correct!\n");
  
  return 0;
}
