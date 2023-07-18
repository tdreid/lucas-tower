from stack import Stack

print("\nWould you like to play a game?")
print("\nLet's play Towers of Hanoi.")

#Create the Stacks
stacks = [Stack('left'), Stack('center'), Stack('right')]

#Set up the Game
number_of_disks = int(input('\nHow many disks do you want to play with?\n'))
while number_of_disks < 3:
  number_of_disks = int(input('Enter a number greater than or equal to 3\n'))

for disk in range(number_of_disks, 0, -1):
  stacks[0].push(disk)

optimal_number_of_moves = 2 ** number_of_disks - 1

message = '\nThe fastest you can solve this game is in {0} moves'
print(message.format(optimal_number_of_moves))

#Get User Input
def get_input():
  choices = [stack.get_name()[0] for stack in stacks]
  while True:
    for i in range(len(stacks)):
      name = stacks[i].get_name()
      letter = choices[i]
      print('"Enter {0} for {1}'.format(letter, name))
    user_input = input('')
    for i in range(len(stacks)):
      if user_input == choices[i]:
        return stacks[i]
        
#Play the Game
num_user_moves = 0
while stacks[2].get_size() != number_of_disks:
  print('\n\n\n...Current Stacks...')
  for stack in stacks:
    stack.print_items()
  while True:
    print('"\nWhich stack do you want to move from?\n"')
    from_stack = get_input()
    print('\nWhich stack do you want to move to?\n')
    to_stack = get_input()
    if from_stack.is_empty():
      print('\n\nThere is no disk on that stack. Try Again')
    if to_stack.is_empty() or from_stack.peek() < to_stack.peek():
      disk = from_stack.pop()
      to_stack.push(disk)
      num_user_moves+=1
      break
    else:
      print('\n\nCannot place smaller disk on top of larger disk. Try Again')
message = '\n\nYou completed the game in {0} moves, and the optimal number of moves is {1}'
print(message.format(num_user_moves, optimal_number_of_moves))
