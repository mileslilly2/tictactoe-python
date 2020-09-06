def main():    
    grid = [[], [], []]
    create_board(grid)
    print_board(grid)
    play(grid)
    
    
def play(grid):
  winner = False
  entered = False
  xMove = True
  numMove = 0
  while not winner:
    if xMove:
      move = "X"
      xMove = False
    else:
      move = "O"
      xMove = True
    print("Enter the coordinates:")
    x, y = input().split()
    try:
      x = int(x)
      y = int(y)
      if x > 0 and x < 4 and y > 0 and y < 4:
        j = x - 1
        i =  3 - y
        if grid[i][j] == " " or grid[i][j] == "_":
          grid[i][j] = move
          numMove += 1 
          print_board(grid)
        else:
          print("This cell is occupied! Choose another one!")
      else:
        print("Coordinates should be from 1 to 3!")
    except:
      print("You should enter numbers!")
    winner = check_board(grid)
    if numMove >= 9 and not winner:
      print("Draw")
      break

def check_board(grid): #to compute the winner and number of winners
  count_wins = 0
  diag_cond1 = grid[0][0] == grid[1][1] == grid[2][2] and grid[1][1] != " " 
  diag_cond2 =  grid[2][0] == grid[1][1] == grid[0][2] and grid[1][1] != " "
  diag_winner = diag_cond1 or diag_cond2
  if diag_winner:
    winner = grid[1][1]
    count_wins += 1
  for i in range(3): #check row and col winners
    if grid[0][i] == grid[1][i] == grid[2][i] and grid[0][i] != " ":
      winner = grid[1][i]
      count_wins += 1
    elif grid[i][0] == grid[i][1] == grid[i][2] and grid[i][0] != " ":
      winner = grid[i][1]
      count_wins += 1
 
  if count_wins == 1:
    print(winner, "wins") 
    return True
  

def create_board(grid):
  count = 0
  for i in range(3):
    for j in range(3):
        grid[i].append(" ")
      
def print_board(grid): 
  print("---------")      
  for row in grid:
    print("|", row[0], row[1], row[2], "|")
  print("---------")


if __name__ == "__main__":
 
    main()
