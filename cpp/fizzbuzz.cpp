#include <iostream>


int main() {
  long amount = 0;
  
  std::cout << "FizzBuzz." << std::endl;
  std::cout << "How high would you like to go?" << std::endl;
  std::cin >> amount;

  for (long i = 0; i <= amount; i++) {
    if (i % 15 == 0) {
      std::cout << "FizzBuzz" << std::endl;
    } else if (i % 3 == 0) {
      std::cout << "Fizz" << std::endl;
    } else if (i % 5 == 0) {
      std::cout << "Buzz" << std::endl;
    } else {
      std::cout << i << std::endl;
    }
  }

  return 0;
}