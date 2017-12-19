# Alexandra Fuhs
# Dec 5th, 2017
# Raspi's Cave Adventure
# A text-based adventure game. 

def left_cave():
    print ("You walk into the left cave. It is cold and dark.")
    # River Choice
    print ("The cave opens up to a large room with an underground river.")
    print ("You notice a small boat on the edge of the river.")
    print ("Do you use the boat, swim, or walk along the side of the river?")
    choice = input("Enter B for boat, S for swim, or W for walk: ").upper()
    return choice
def wrong_answer():
    print ("You are standing there because you don't know where to go...")
    print ("...Suddenly a random stalactite falls from the ceiling killing you instantly!")
    print ("GAME OVER!!!")
def right_cave():
    print ("You walk into the right cave. It is cold and dark.")
    # Rope and Torch Choice
    print ("You see a hole with a rope going down and a torch off in the distance.")
    print ("Do you want to walk to the torch or climb down the rope?")
    choice = input("Enter T for torch or R for rope: ").upper()
    return choice
def torch_death():
    '''This is the player's death when they walk to the torch'''
    print ("You reach for the torch and feel a knife stab deep into your back.")
    print ("You turn around and see a strange creature standing over you...")
    print ("It turns out to be an old hag who lives in a cave....")
def dragons_lair():
    '''This is the player's choice of whether to fight the dragon or not.'''
    print ("You see the dragon sleeping and a dark room off to the side.")
    input ("Do you want to slay the dragon or go to the dark room? ")
    choice = input ("Enter S for slay or R for room.").upper()
    return choice
    
    

# Title Screen
print ("""


 







██████╗  █████╗ ███████╗██████╗ ██╗███████╗     ██████╗ █████╗ ██╗   ██╗███████╗     █████╗ ██████╗ ██╗   ██╗███████╗███╗   ██╗████████╗██╗   ██╗██████╗ ███████╗
██╔══██╗██╔══██╗██╔════╝██╔══██╗██║██╔════╝    ██╔════╝██╔══██╗██║   ██║██╔════╝    ██╔══██╗██╔══██╗██║   ██║██╔════╝████╗  ██║╚══██╔══╝██║   ██║██╔══██╗██╔════╝
██████╔╝███████║███████╗██████╔╝██║███████╗    ██║     ███████║██║   ██║█████╗      ███████║██║  ██║██║   ██║█████╗  ██╔██╗ ██║   ██║   ██║   ██║██████╔╝█████╗  
██╔══██╗██╔══██║╚════██║██╔═══╝ ██║╚════██║    ██║     ██╔══██║╚██╗ ██╔╝██╔══╝      ██╔══██║██║  ██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║   ██║   ██║   ██║██╔══██╗██╔══╝  
██║  ██║██║  ██║███████║██║     ██║███████║    ╚██████╗██║  ██║ ╚████╔╝ ███████╗    ██║  ██║██████╔╝ ╚████╔╝ ███████╗██║ ╚████║   ██║   ╚██████╔╝██║  ██║███████╗
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝╚══════╝     ╚═════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝    ╚═╝  ╚═╝╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝
                                                                                                                                                                 
""")
import time


print ("You're taking a walk when you notice a cave. You walk into the cave...")


# 1st Choice
print ("You see the cave split into a left and right tunnel.")
print ("Do you choose to go left or right?")
cave_choice = input ("Enter R for right or L for left: ").upper()
if cave_choice == "L" or cave_choice == "LEFT":
    # Left cave
    choice = left_cave()    
    
    if choice == "B" or choice == "BOAT":
        # Boat Choice
        print ("You climb into the wooden boat and push off.")
        # Death Scene
        print ("You are happily sailing along in the boat...")
        time.sleep(2)
        
    elif choice == "S" or choice == "SWIM":
        # Swim Choice
        print ("You take a deep breath and dive into the cold river.")
        print ("You just realized that you skipped your medieval swim lessons.")
        print ("But you find that the doggy paddle works well...")
        # Get the treasure
    elif choice == "W" or choice == "WALK":
        print ("You start walking along the narrow edge of the river.")
        # Death Scene
        wrong_answer()
    else:
          # Wrong answer
          wrong_answer()
         
        

    
elif cave_choice == "R" or cave_choice == "RIGHT":
    # Right cave
    print ("You walk into the right cave.")
    print ("The cave starts sloping downward.")
    choice = right_cave()
    if choice == "T" or choice == "TORCH":
        print ("You walk towards the torch slowly.")
        #TODO: Add death function for TORCH
        torch_death()
    elif choice == "R" or choice == "ROPE":
        print ("You grab the rope and lower yourself down the hole.")
        print ("You hear a dragon breathing in the dark room.")
        #TODO: Add Dragon Choice
        choice = dragons_lair()
        if choice == "S" or choice == "SLAY":
            print ("You die!")
        elif choice == "R" or choice == "ROOM":
            print ("You win!")
        else:
                wrong_answer()
        
    else: # Wrong input
        wrong_answer()
    
else:
    # Wrong answer
    wrong_answer()

