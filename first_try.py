import random

def intro_screen():
  print('                   PLAY NIM!!')
  print('*****************************************************')
  print('Force the computer to choose the last star to win!!!')
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

#intro_screen()
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
      