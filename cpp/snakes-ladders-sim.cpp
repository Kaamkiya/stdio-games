/**
 * @name Snakes and Ladders Simulator
 * @version 0.0.3
 * @author Kaamkiya
 */

#include <iostream>
#include <vector>
#include <algorithm>

/**Return a random number between 1 and 6*/
int roll_dice() {
  // set up a random seed so that the random numbers are different
  srand((unsigned) time(NULL) * rand());
  return rand() % 6 + 1;
}

int main() {
  // vectors with amount of things
  std::vector<int> amount_of_moves {};
  
  // ladders' starting points
  std::vector<int> ladders_from {4, 13, 33, 42, 50, 62, 74};
  // ladders' ending points
  std::vector<int> ladders_to {25, 46, 49, 63, 69, 81, 92};

  // snakes' starting points
  std::vector<int> snakes_from {27, 40, 43, 54, 66, 76, 89, 99};
  // snakes' ending points
  std::vector<int> snakes_to {5, 3, 18, 31, 45, 58, 53, 41};
  
  int sims_to_run = 0;
  
  // introduce the program
  std::cout << "Welcome to the snakes and ladders simulator!" << std::endl;
  std::cout << "The goal of this program is to find the average amount of ";
  std::cout << "moves required to win a snakes and ladders game." << std::endl;
  std::cout << "How many simulations would you like to run?" << std::endl;
  std::cout << "> ";
  std::cin >> sims_to_run; // get the amount of simulations to run
  
  for (int i = 0; i < sims_to_run; i++) {
    if (i % 1000 == 0) {
      // if 1000 simulations have been run, alert the user
      std::cout << i << " simulations run..." << std::endl;
    }
    
    int moves_taken = 0;
    int pos = 1;
    int steps_to_move = 0;
    
    while (pos != 100) { // main game loop (very simple, isn't it?)
      moves_taken++;
      
      steps_to_move = roll_dice();
      
      if (steps_to_move + pos > 100) {
        continue;
      }
      pos += steps_to_move;
      
      for (int i = 0; i < ladders_from.size(); i++) {
        if (pos == ladders_from[i]) { // if player is on ladder
          pos = ladders_to[i]; // move playerto end of ladder
        }
      }
      for (int i = 0; i < snakes_from.size(); i++) {
        if (pos == snakes_from[i]) {
          pos = snakes_to[i]; // same as above for snakes
        }
      }
    }
    amount_of_moves.push_back(moves_taken); // add the amount of moves used to the list
  }
  std::cout << sims_to_run << " simulations run." << std::endl;
  
  long total_moves = 0;
  
  for (auto amount: amount_of_moves) {
    total_moves += amount;
  }
  
  std::cout << "Each game took an average of " <<
    total_moves / sims_to_run <<
    " moves to win." <<
    std::endl;
    
  std::cout << "The longest game lasted " << *std::max_element(amount_of_moves.begin(), amount_of_moves.end()) << " moves." << std::endl;
  std::cout << "The shortest game lasted " << *std::min_element(amount_of_moves.begin(), amount_of_moves.end()) << " moves." << std::endl;

  return 0;
}
