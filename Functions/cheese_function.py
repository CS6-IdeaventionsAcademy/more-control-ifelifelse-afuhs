# Alexandra Fuhs
# 12/12/17
# Function Practice :)

import math

def cheese ():
    '''Makes a screen full of I like cheeses!'''
    print ("I like cheese!" * 100)


def temp_C(temp_F):
    '''Coverts a temperature in Fahrenheit to Celsius'''
    answer = (temp_F - 32) * (5/9)
    return answer


def volume_sphere(radius):
    '''Calculates the volume of a sphere radius is an integer or float'''
    volume = (4/3) *math.pi *r**3
    return volume

def pigs ():
    '''Makes pigs'''
    print ("pig" * 1)
    
    

#cheese()

x = input ("Please enter a temperature in Fahrenheit: ")
x = float (x) # Converting the input to a float "52.0" --> 52.0
t_in_C = temp_C(x)
print ("That temperature in Celsius is", t_in_C)

r = input("Please enter a radius of a sphere: ")
r = float (r)
v_sphere = volume_sphere (r)
print ("The volume of the sphere is", v_sphere)

p = input ("Do you like pigs?")














