# set up constants
PLAYER = "@" # how the player is displayed
BLOCK = 9608.chr("UTF-8") # how the walls are shown
WALL = "#" # what a wall is defined by inthe maze
EMPTY = " " # how hallways are defined in the maze
MAZE = [
  "##########".split(""),
  "#S#      #".split(""),
  "#   # # ##".split(""),
  "####   # #".split(""),
  "#        #".split(""),
  "# #  #####".split(""),
  "####     #".split(""),
  "#    #####".split(""),
  "#E#      #".split(""),
  "##########".split("")
]

playerx = -1
playery = -1
exitx = -1
exity = -1

(0..9).each do |x|
  (0..9).each do |y|
    if MAZE[x][y] == "S"
      playerx = x # find the starting point and make the player go there
      playery = y
    end
    if MAZE[x][y] == "E"
      exitx = x # find the exit and set up it's coordinates
      exity = y
    end
  end
end

def draw_maze(px, py)
  (0..9).each do |i|
    (0..9).each do |j|
      if i == px and j == py
        print PLAYER
      elsif MAZE[i][j] == WALL
        print BLOCK
      elsif MAZE[i][j] == EMPTY
        print " "
      else
        print MAZE[i][j]
      end
    end
    puts
  end
  puts
end

while true # main game loop
  draw_maze(playerx, playery)
  
  puts "Where would you like to go?"
  puts "  W"
  puts "A   D"
  puts "  S"
  
  print "> " # prompt the user
  move = gets.chomp.downcase # get user's input, remove whitespace, and lowercase it
  
  if not ["w", "a", "s", "d"].include?(move)
    puts "\033[33mInvalid move." # \033[33m is the ANSI escape code for yellow
    print "\033[0m" # \033[0m is the ANSI escape code for reset
    next
  end
  
  if move == "a"
    if MAZE[playerx][playery - 1] == WALL
      puts "\033[33mYou can't go there, that spot's taken."
      print "\033[0m"
    else
      playery -= 1
    end
  elsif move == "d"
    if MAZE[playerx][playery + 1] == WALL
      puts "\033[33mYou can't go there, that spot's taken."
      print "\033[0m"
    else
      playery += 1
    end
  elsif move == "w"
    if MAZE[playerx - 1][playery] == WALL
      puts "\033[33mYou can't go there, that spot's taken."
      print "\033[0m"
    else
      playerx -= 1
    end
  elsif move == "s"
    if MAZE[playerx + 1][playery] == WALL
      puts "\033[33mYou can't go there, that spot's taken."
      print "\033[0m"
    else
      playerx += 1
    end
  end
  
  if [playerx, playery] == [exitx, exity]
    # if the player is on the exit
    draw_maze(playerx, playery)
    puts "\033[32mYou Win!" # tell them they won
    exit # and exit the program
  end
end
