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

player_input=int(input("What Number? "))
print(f"You picked {player_input}")
print()

if player_input in range(1,3):
    print("Your in row one!")
elif player_input in range(4,6):
    print("Your in row two!")
elif player_input in range(7,9):
    print("Your in row three!")
