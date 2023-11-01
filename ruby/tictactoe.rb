BOARD = [
  [' ', ' ', ' '],
  [' ', ' ', ' '],
  [' ', ' ', ' ']
]

turn = 'to be decided by the code below, which picks it randomly'
if rand(0..1) == 0
  turn = 'o'
else
  turn = 'x'
end

def check_for_win()
  (0..2).each do |i|
    if BOARD[i] == ['x', 'x', 'x'] # check each row for a solid win
      return 'x'
    elsif BOARD[i] == ['o', 'o', 'o']
      return 'o'
    end
  end
  
  amount_of_x = 0
  amount_of_o = 0
  
  (0..2).each do |i|
    (0..2).each do |j|
      if BOARD[i][j] == 'x' # check each column
        amount_of_x += 1
      elsif BOARD[i][j] == 'o'
        amount_of_o += 1
      end
    end
  end
  
  if amount_of_x == 3
    return 'x'
  end
  if amount_of_o == 3
    return 'o'
  end
  
  amount_of_x = 0
  amount_of_o = 0
  
  (0..2).each do |i| # check top-left to bottom-right diagonal
    if BOARD[i][i] == 'x'
      amount_of_x += 1
    elsif BOARD[i][i] == 'o'
      amount_of_o += 1
    end
  end
  
  if amount_of_x == 3
    return 'x'
  end
  if amount_of_o == 3
    return 'o'
  end
end

def draw_board()
  puts BOARD[0][0] + '|' + BOARD[0][1] + '|' + BOARD[0][2] # first row of board
  puts '- - -' # the lines between the rows of the board
  puts BOARD[1][0] + '|' + BOARD[1][1] + '|' + BOARD[1][2]
  puts '- - -'
  puts BOARD[2][0] + '|' + BOARD[2][1] + '|' + BOARD[2][2]
end


while true # main game loop
  puts "#{turn}'s turn"
  draw_board()

  x = -1
  y = -1
  
  while true # loop until a valid answer is given
    puts 'Enter the y-position you want to go to:'
    print '> '
    x = Integer(gets.chomp) rescue false # convert input to number, if fail, return false
    if not x # if the input was not a number
      next # continue through the loop
    end
    if 0 <= x and x <= 2
      break
    end
  end
  while true # same as for x position
    puts 'Enter the x-position you want to go to:'
    print '> '
    y = Integer(gets.chomp) rescue false
    if not y
      next
    end
    if 0 <= y and y <= 2
      break
    end
  end

  if BOARD[x][y] == ' '
    BOARD[x][y] = turn
  end
  
  who_won = check_for_win()
  if who_won == 'x'
    puts 'x wins!'
    exit
  end
  if who_won == 'o'
    puts 'o wins!'
    draw_board()
    exit
  end
  
  if turn == 'x'
    turn = 'o'
  else
    turn = 'x'
  end
end
