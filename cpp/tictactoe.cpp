#include <iostream>
#include <vector>
#include <algorithm>

void print_board(std::vector<std::vector<std::string>> board) {
  std::cout << board[0][0] << "|" << board[0][1] << "|" << board[0][2] << " 123" << std::endl;
  std::cout << "- - -" << std::endl;
  std::cout << board[1][0] << "|" << board[1][1] << "|" << board[1][2] << " 456" << std::endl;
  std::cout << "- - -" << std::endl;
  std::cout << board[2][0] << "|" << board[2][1] << "|" << board[2][2] << " 789" << std::endl;
}

char game_won(std::vector<std::vector<std::string>> board){
  int x = 0, o = 0;

  for (int i = 0; i < board.size(); i++) {
    if (board[i][0] == "x" && board[i][1] == "x" && board[i][2] == "x") {
      return 'x';
    }
    if (board[i][0] == "o" && board[i][1] == "o" && board[i][2] == "o") {
      return 'o';
    }
  }
  
  for (int i = 0; i < board.size(); i++) {
    if (board[0][i] == "x" && board[1][i] == "x" && board[2][i] == "x") {
      return 'x';
    }
    if (board[0][i] == "o" && board[1][i] == "o" && board[2][i] == "o") {
      return 'o';
    }
  }
  
  for (int i = 0; i < board.size(); i++) {
    if (board[i][i] == "x") {
      x++;
    }
    if (board[i][i] == "o") {
      o++;
    }
  }
  
  if (x == 3) {
    return 'x';
  } else if (o == 3) {
    return 'o';
  }
  
  if (board[0][2] == "x" && board[1][1] == "x" && board[2][0] == "x") {
    return 'x';
  }
  
  if (board[0][2] == "o" && board[1][1] == "o" && board[2][0] == "o") {
    return 'o';
  }
  
  return ' ';
}

int main() {
  std::string turn = "x";
  
  std::vector<std::vector<std::string>> board = {
    {" ", " ", " "},
    {" ", " ", " "},
    {" ", " ", " "}
  };
  
  while (true) {
    print_board(board);
    int pos;
    std::cout << turn << "'s turn." << std::endl;
    std::cout << "Enter your position: ";
    std::cin >> pos;
    std::cout << std::endl;
    
    int posx, posy;
    
    switch(pos){
      case 1: posx = 0; posy = 0; break;
      case 2: posx = 0; posy = 1; break;
      case 3: posx = 0; posy = 2; break;
      case 4: posx = 1; posy = 0; break;
      case 5: posx = 1; posy = 1; break;
      case 6: posx = 1; posy = 2; break;
      case 7: posx = 2; posy = 0; break;
      case 8: posx = 2; posy = 1; break;
      case 9: posx = 2; posy = 2; break;
      default:
        std::cout << "Invalid Move" << std::endl;
        break;
        continue;
    }
    
    if (board[posx][posy] != " ") {
      std::cout << "That spot is taken, sorry." << std::endl;
      continue;
    } else {
      board[posx][posy] = turn;
    }
    
    if (game_won(board) == 'x') {
      print_board(board);
      std::cout << "x wins!" << std::endl;
      break;
    }
    
    if (game_won(board) == 'o') {
      print_board(board);
      std::cout << "o wins!" << std::endl;
      break;
    }
    
    if (turn == "x") {
      turn = "o";
    } else {
      turn = "x";
    }
  }
  
  return 0;
}
