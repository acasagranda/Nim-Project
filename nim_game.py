import random
import time
import math

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
    row_sizes = [random.randint(1,10) for i in range(3)]
    return row_sizes

def print_screen(row_size):
  print('\nROW 1: ',end=' ')
  for i in range(row_size[0]):
    print('*', end=' ')
  print('\nROW 2: ',end=' ')
  for i in range(row_size[1]):
    print('*', end=' ')
  print('\nROW 3: ',end=' ')
  for i in range(row_size[2]):
    print('*', end=' ')
  print('\n')

def determine_player_move(row_size):
    player_row = -1
    while player_row not in [1,2,3]:
      player_row = input('From which row do you want to remove stars on this turn? (1, 2, or 3): ')
      if player_row.isdigit():
        player_row = int(player_row)
        if player_row in [1,2,3]:
          if row_size[player_row-1] == 0:
            print("There are no stars left in this row, choose again.")
            player_row = -1
    player_num = -1
    while player_num not in range(1,row_size[player_row-1]+1):
      question = 'How many stars do you want to remove from Row ' + str(player_row) + '? '
      player_num = input(question)
      if player_num.isdigit():
        player_num = int(player_num)
    return player_row,player_num

#convert row sizes to binary string
def rows_to_binary(row_size):
  #find the number of digits each binary number would be
  num_binary_digits = []
  for row in row_size:
    if row == 0:
      num_binary_digits.append(0)
    else:
      num_binary_digits.append(int(math.floor(math.log2(row)))+1)
  #find the maximun of those digits
  max_digits = max(num_binary_digits)
  #make a list of the row sizes in a binary string and add any needed leading zeros to make all the same size
  row_binary_string = []
  for index in range(3):
    row_binary = "{0:b}".format(int(row_size[index]))
    binary_string = []
    diff = max_digits - num_binary_digits[index]
    for i in range(diff):
        binary_string.append(0)
    for digit in row_binary:
        binary_string.append(int(digit))
    row_binary_string.append(binary_string)
  return row_binary_string,max_digits

#given the current board decide the computer's best move
def determine_comp_move(row_size):
  #change the decimal row values to binary, max_digits is the number of digits in the largest number
  row_binary_string, max_digits = rows_to_binary(row_size)
  #for each place value add up the digits in all rows
  sum_rows = []
  for digit in range(max_digits):
    sum = 0
    for num in row_binary_string:
      sum += num[digit]
    sum_rows.append(sum)
  #find largest row
  row_choice = row_size.index(max(row_size))
  #calculate what the new row needs to be
  new_row_list = []
  for i in range(max_digits):
    if sum_rows[i]%2 == 0:
      new_row_list.append(row_binary_string[row_choice][i])
    else:
      new_row_list.append(1 - row_binary_string[row_choice][i])
  #put new_row into a string
  new_row_str = ""
  for num in new_row_list:
    new_row_str += str(num)
  #change new_row string into a decimal number
  new_row_num = int(new_row_str,2)
  computer_num = row_size[row_choice] - new_row_num
  #If computer_num is 0 there is no good move so just remove 1
  if computer_num == 0:
    computer_num = 1
  return row_choice, computer_num

def check_win(row_size):
  winner = False
  sum_size = 0
  for size in row_size:
    sum_size += size
  if sum_size == 0:
    winner = True
  return winner



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

winner = 'neither'
while winner == 'neither':
  if player_turn == 1:
    player_row,player_num = determine_player_move(row_size)
    row_size[player_row-1] -= player_num
    print_screen(row_size)
    time.sleep(5)
    player_turn = 0
    if check_win(row_size):
      winner = 'player'
  else:
    computer_row,computer_num = determine_comp_move(row_size)
    row_size[computer_row] -= computer_num
    print('The computer chooses to remove {num1} stars from row {row}.'.format(num1 = computer_num,row = computer_row+1))
    print_screen(row_size)
    player_turn = 1
    if check_win(row_size):
      winner = 'computer'
if winner == 'player':
  print('\n\nWell done, you win!!!')  
else:
  print('\n\nThe computer wins this one.')
    
    