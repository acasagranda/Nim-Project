import random
import time

def intro_screen():
  print('                   PLAY NIM!!')
  print('*****************************************************')
  print('         Remove the last star to win!!!')
  print('*****************************************************')
  ready_to_play = False
  while ready_to_play == False:
    instructions = input('\nDo you want to see instructions on how to play?(Y or N): ')
    if instructions == 'Y' or instructions == 'y':
      ready_to_play = True
      print('\nPlayers take turns removing stars from the board.')
      print('During a turn, players may choose stars from ONLY ONE row.')
      print('During a turn, players must remove at least one star but may remove up to all the stars in the row of their choice.')
    elif instructions == 'N' or instructions == 'n':
      ready_to_play = True
  
def choose_row_sizes():
    row_sizes = [random.randint(1,10) for i in range(4)]
    return row_sizes

def print_screen(row_size):
  print('\nROW 1: ',end=' ')
  for i in range(row_size[1]):
    print('*', end=' ')
  print('\nROW 2: ',end=' ')
  for i in range(row_size[2]):
    print('*', end=' ')
  print('\nROW 3: ',end=' ')
  for i in range(row_size[3]):
    print('*', end=' ')
  print('\n')



def determine_player_turn():
    player_row = -1
    while player_row not in [1,2,3]:
      player_row = input('From which row do you want to remove stars on this turn? (1, 2, or 3): ')
      if player_row.isdigit():
        player_row = int(player_row)
        if player_row in [1,2,3]:
          if row_size[player_row] == 0:
            print("There are no stars left in this row, choose again.")
            player_row = -1
        
    player_num = -1
    while player_num not in range(1,row_size[player_row]+1):
      question = 'How many stars do you want to remove from Row ' + str(player_row) + '? '
      player_num = input(question)
      if player_num.isdigit():
        player_num = int(player_num)
    return player_row,player_num

intro_screen()
row_size = choose_row_sizes()
print_screen(row_size)
choose_turn = False
while choose_turn == False:
  turn = input('Do you want to go first? (Y or N):')
  if turn == 'Y' or turn == 'y':
      player_turn = 1
      choose_turn = True
  elif turn == 'N' or turn == 'n':
      player_turn = 0
      choose_turn = True
is_winner = False
while not is_winner:
  if player_turn == 1:
    player_row,player_num = determine_player_turn()
    row_size[player_row] -= player_num
    print_screen(row_size)
    time.sleep(5)
    player_turn = 0
  else:
    #this is where the computer calcs its move 
    print('comp')
    break
    
    
    