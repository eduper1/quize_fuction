#abdullahi, 10, kenya

# This function is to ask the user wether to play or not?
def is_playing():
    # Know what the user want by asking
    will_play = input("Do you want to play? ")
    # store "yes" value in play variable
    play = "yes"
    
    # Compare the will_play variable to play
    # if True, show " let play!!!"
    if will_play == play:
        print("les tart to play!!!!!!.")
    # if above condition is not True,
    # The user don't want to play.
    # show 'You are done' and quit the game    
    else:
        print("you are done!!!!")
        quit()

# Test is_playing function
# is_playing()

# Create a function that asks the user some questions,
# but only if the user want to play
def quiz():
    is_playing()
    
    # Question one
    question = input("What is the brightest object in the night sky? ")
    # True answer
    answer = "moon"
    
    # Check user's answer with comparing True answer
    # if the user got it wrong, show 'sorry try again'
    if question != answer:
        print(f"Sorry,{question} is not true answer, try again!")
    
    # if the above condition is False, 
    # the user got it right
    else:
        print(f"Correct!!! {question} is true.")    
    
# test quiz function
quiz()