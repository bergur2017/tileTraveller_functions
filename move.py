LEFT_BOUNDARY = 1
RIGHT_BOUNDARY = 10
 
def print_instructions(): #function prints out instructions for player
    print("l - for moving left")
    print("r - for moving right")
    print("Any other letter for quitting")
def print_new_pos(new_pos):
    print("New position is: " + str(new_pos))
def calc_new_pos(position, movement):
        if movement == "l":
            if position == LEFT_BOUNDARY:
                return position
            else:
                return position - 1
        if movement == "r":
            if position == RIGHT_BOUNDARY:
                return position
            else:
                return position + 1
def input_movement():
    move =  input("Input your choice: ")
    return move
def input_pos():
    position = int(input("Input a position between 1 and 10: "))
    return position


pos = input_pos()

print_instructions()

movement = input_movement()

while movement == "l" or movement == "r":
    pos = calc_new_pos(pos,movement)
    print_new_pos(pos)
    print_instructions()
    movement = input_movement()
if movement != "l" and movement != "r":
    print_new_pos(pos)




    