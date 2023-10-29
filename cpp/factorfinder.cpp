#include <iostream>
#include <vector>
#include <algorithm>

std::vector<int> find_factors(long number) {
  std::vector<int> factors {};
  
  for (long i = 1; i * i <= number; i++) {
    if (number % i == 0) {
      factors.push_back(i);
      if (number / i != i) {
        factors.push_back(number / i);
      }
    }
  }
  
  std::sort(factors.begin(), factors.end());
  return factors;
}

int main() {
  long n = 0;
  
  std::cout << "Welcome to the factor finder program!" << std::endl;
  std::cout << "Enter a number to find the factors of: ";
  std::cin >> n;
  
  std::vector<int> factors = find_factors(n);
  
  for (int f: factors) {
    std::cout << f << std::endl;
  }
  
  if (factors.size() == 0) {
    std::cout << "That number has no factors." << std::endl;
  }
  
  while (true) {
    char again = ' ';
    std::cout << "Would you like to go again? (y/n)" << std::endl;
    std::cin >> again;
    if (again == 'y') {
      main();
    } else if (again == 'n') {
      std::cout << "Thanks for using this!" << std::endl;
      break;
    }
  }
  
  return 0;
}