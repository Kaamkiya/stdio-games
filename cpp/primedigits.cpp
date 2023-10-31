#include <iostream>

bool is_prime(long n) {
  for (int i = 2; i < n; i++) {
    if (n % i == 0) {
      return false;
    }
  }
  return true;
}

int main() {
  long amount = 0;
  
  std::cout << "This project shows all of the prime numbers up to a number." << std::endl;
  std::cout << "How high would you like to go?" << std::endl;
  
  std::cout << "> ";
  std::cin >> amount;
  
  for (long i = 1; i <= amount; i++) {
    if (is_prime(i)) {
      std::cout << i << " ";
    }
  }
  
  std::cout << std::endl;
  
  return 0;
}