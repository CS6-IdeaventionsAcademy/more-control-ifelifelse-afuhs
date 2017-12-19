print ("*" * 68)
print (" Welcome to the Game Show! Please pick a door and choose your prize!")
print ("*" * 68)

door_a = "Doorknob"
door_b = "New Car"
door_c = "Frozen Meatloaf"
door_d = "$100,000"
door_e = "Vacation to Hawaii"

play_again = "Yes"





while play_again == "Yes":
    player_choice = input ("Please choose a door! (Type A, B, C, or D) ")
    if player_choice == "A":
        print ("Congratulations! You won a doorknob!")
    elif player_choice == "B":
        print ("Congratulations! You won a new car!")
    elif player_choice == "C":
        print ("Congratulations! You won frozen meatloaf!")
    elif player_choice == "D":
        print ("Congratulations! You won $100,000!")
    elif player_choice == "E":
        print ("Congratulations! You opened the Mystery Door and won a vacation to Hawaii!")
    else:
        print ("CHOOSE A DOOR!!!!!!!!!")
    play_again = input ("Would you like to play again? ")
    
