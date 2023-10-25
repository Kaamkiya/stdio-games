#include <iostream>
#define PLAYER '@'
#define WALL '#'
#define EMPTY ' '
#define BLOCK ' '

void draw_maze(char maze[11][11], int px, int py) {
  for (int i=0; i<10; i++) {
    for (int j=0; j<10; j++) {
      if (px == i && py == j) {
        std::cout << PLAYER; // if the player is in that spot, draw their image
      } else {
        std::cout << maze[i][j]; // else, draw either the wall or nothing
      }
    }
    std::cout << std::endl; // print a new line after each row
  }
  
  std::cout << std::endl; // print a new line after the maze
}

int find_in_maze(char maze[11][11], char query, char x_or_y) {
  for (int i=0; i<10; i++) {
    for (int j=0; j<10; j++) {
      if (maze[i][j] == query) {
       if (x_or_y == 'y') {
         return i;
       }
       return j;
      }
    }
  }
  
  return -1; // return this as a fallback for not found
}

int main() {
  char MAZE[11][11] = {
    "##########",
    "#S#      #",
    "#   # # ##",
    "####   # #",
    "#        #",
    "# #  #####",
    "####     #",
    "#    #####",
    "#E#      #",
    "##########"
  };
  
  char dir = ' '; // direction the player want to go
  
  int playerx = find_in_maze(MAZE, 'S', 'x');
  int playery = find_in_maze(MAZE, 'S', 'y');
  
  int exitx = find_in_maze(MAZE, 'E', 'y');
  int exity = find_in_maze(MAZE, 'E', 'x');
  
  while (true) {
    draw_maze(MAZE, playerx, playery);
    
    std::cout << "Where would you like to go? (or Q to quit)" << std::endl;
    std::cout << "  W" << std::endl;
    std::cout << "A   D" << std::endl;
    std::cout << "  S" << std::endl;
    
    std::cout << std::endl << "> ";
    std::cin >> dir;
    
    dir = toupper(dir);
    
    if (!(dir == 'W'||dir == 'A'||dir == 'S'||dir == 'D'||dir == 'Q')) {
      std::cout << "That is an invalid direction." << std::endl;
      continue;
    }
    if (dir == 'A') {
      if (MAZE[playerx][playery-1] != WALL) {
        playery--;
      } else {
        std::cout << "That spot is taken, sorry." << std::endl;
      }
    }
    if (dir == 'D') {
      if (MAZE[playerx][playery+1] != WALL) {
        playery++;
      } else {
        std::cout << "That spot is taken, sorry." << std::endl;
      }
    }
    if (dir == 'W') {
      if (MAZE[playerx-1][playery] != WALL) {
        playerx--;
      } else {
        std::cout << "That spot is taken, sorry." << std::endl;
      }
    }
    if (dir == 'S') {
      if (MAZE[playerx+1][playery] != WALL) {
        playerx++;
      } else {
        std::cout << "That spot is taken, sorry." << std::endl;
      }
    }
    
    if (dir == 'Q') {
      return 0;
    }
    
    if (playerx == exitx && playery == exity) {
      std::cout << "You won! Thanks for playing!" << std::endl;
      return 0;
    }
  }
  
  // std::cout << exitx << ", " << exity << std::endl;
  // std::cout << playerx << ", " << playery << std::endl;
  
  draw_maze(MAZE, playerx, playery);

  return 0;
}
