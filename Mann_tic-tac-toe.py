"""
# for this assignment, I think I will split this program into three different groups 
# One thru three, two thru six, and six thru nine.
# First, I will ask the user to give me a number, then assign that number to a function acording to their input.  

The program will print out three rows, 
and then using a for loop, will replace numbers with letters in the row acording to user input
"""
player_input=None
row_one=[1,2,3]
row_two=[4,5,6]
row_thr=[7,8,9]

print(row_one)
print(row_two)
print(row_thr)

range_1=range(1,4)
range_2=range(3,7)
range_3=range(6,10)

def player_one_input():
    player_input=int(input("What Number? "))
    print(f"You picked {player_input}")
    print()
    return player_input

def row_parser():
    if player_input in range_1:
        print("Your in row one!")
        print()
    elif player_input in range_2:
        print("Your in row two!")
        print()
    elif player_input in range_3:
        print("Your in row three!")
        print()
    else:
        print("Not Valid")
row_parser()