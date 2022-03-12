import random

print("     ________________________________     ")
print("     |                              |     ")
print("     |                              |     ")
print("     |       Penalty Shootout       |     ")
print("     |                              |     ")
print("_____|______________________________|_____")
print("")
print("")
#Let the computer decides where it wants the goal to dive
options=["TL","BL","M","TR","BR"]
computerOption = random.choice(options)
score = 0
for i in range(0,5):
    # Now let's ask the user where they want to shoot
    useroption = input("Where would yo like to shoot? TL Bl M Tr or Br")

    # Then we can check if the goal blocked the ball or not
    if computerOption == useroption:
        print('The goalie blocked the penalty shootout')
    else:
        print('You scored a goal')
        score += 1
        print(f'Your score is {score}')

