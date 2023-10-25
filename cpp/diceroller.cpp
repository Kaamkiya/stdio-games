#include <iostream>

int main() {
  long amount_of_sides = 0L;
  long amount_of_dice = 0L;
  
  std::cout << "How many dice would you like to roll?" << std::endl;
  try {
    std::cout << "> "; // add a cool prompt to the input
    std::cin >> amount_of_dice;
  } catch (std::exception& e) {
    std::cout << "That's not a valid number." << std::endl;
    return -1; // exit with a failure status if the user enters an invalid number
  }
  
  std::cout << "How many sides should the dice have?" << std::endl;
  try {
    std::cout << "> ";
    std::cin >> amount_of_sides;
  } catch (std::exception& e) {
    std::cout << "That's not a valid number." << std::endl;
    return -1;
  }
  
  long total = 0L;
  
  for (int i = 0; i < amount_of_dice; i++) {
    srand((unsigned) time(NULL)*rand()); // make a random seed
    total += rand() % amount_of_sides + 1; // add a random number (minimum 1) to the total
  }
  
  std::cout << "Total: " << total << std::endl;
  
  std::string go_again = "";
  
  while (!(go_again == "y" || go_again == "n" || go_again == "Y" || go_again == "N")) {
    std::cout << "Would you like to go again? (Y/N)" << std::endl;
    
    std::cout << "> ";
    std::cin >> go_again;
  }
  
  if (go_again == "y" || go_again == "Y") {
    main();
  }
  
  std::cout << "Thanks for playing!" << std::endl;
  return 0;
}
