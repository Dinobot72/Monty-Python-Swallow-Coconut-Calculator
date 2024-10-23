# -*- coding: utf-8 -*-
"""

  Program: CSC115/170 Lab 05
 ----------------------------
  Partner 1:  Dylan Regan
  Partner 2: Hunter Prather
  Date: 20/16/2024
      
      
  **To get full credit:**
        * The code must run without errors
        * You must check for valid swallows and numbers
        * Your code must implement the four functions listed with correct arguments and return values
        * The code must calculate the carry weight, number of coconuts and number of swallows correctly
        * The code will continue running until the user chooses to end (while loop)
        * You must comment your code well
        * You must work as a group
        * You must turn the lab in on time

  
      
      
"""
# Put any import statements here
import math

# ###########################################################
# get_swallows() function header
# - arguments: none
# - returns: swallow type and swallow number
# - Dylan
# ###########################################################
def get_swallows():
    # define varibales and list of correct swallows
    valid_ans = False
    valid_swallows = ["african", "cliff", "european", "fanti", "mosque", "tree", "welcome"]
    
    # Ask for swallow type
    swallow_type = input("Enter type of swallow: ")
    
    # Check for correct swallow type
    while valid_ans != True:
        # Run through the list of correct swallows and check for correct
        for swallow in valid_swallows:
            if swallow == swallow_type.lower():
                valid_ans = True
                break
        if valid_ans != True:
            swallow_type = input("Uknown type '{}'; Please enter type of swallow: ".format(swallow_type))
                
    # Ask for number of swallows
    swallow_amount = int(input("Enter number of swallows: "))

    # Check for swallow amount is above 0
    while swallow_amount < 0:
        swallow_amount = int(input("Number must be above 0; Enter number of swallows: "))
    
    # Returns the selected swallow type in lower case and the amount of swallows
    return swallow_type.lower(), swallow_amount


# ###########################################################
# carry_weight( sw_type, num ) function header
# - parameters: swallow type and number
# - returns: carry weight in grams
# - Dylan
# ###########################################################
def carry_weight(sw_type, num):
    
    #Check for each swallow type and calculate the carry weight
    if sw_type == "african":
        carry_weight = (num * 48)/5
    elif sw_type == "cliff":
        carry_weight = (num * 25)/5
    elif sw_type == "european":
        carry_weight = (num * 20)/5
    elif sw_type == "fanti":
        carry_weight = (num * 9)/5
    elif sw_type == "mosque":
        carry_weight = (num * 58)/5
    elif sw_type == "tree":
        carry_weight = (num * 23)/5
    elif sw_type == "welcome":
        carry_weight = (num * 15)/5
    
    # Returns the carry weight of the specific type of swallow by how many they have
    return carry_weight



# ###########################################################
# num_coconuts( weight, avg_coconut ) function header
# - parameters: carry load, weight of 1 coconut in grams
# - returns: fraction of coconuts that can be carried
# - Hunter
# ###########################################################
def num_coconuts(weight, avg_coconut):
    
    #Gets the amount of coconuts possible
    num_nuts= weight / avg_coconut
    
    return num_nuts



# ###########################################################
# num_swallows ( sw_type, avg_coconut ) function header
# - parameters: type of swallow and weight of 1 coconut in grams
# - returns: the number of swallows needed
# - Hunter
# ###########################################################
def num_swallows(sw_type, avg_coconut):
    
    #Gets the number of swallows
    num_sw=avg_coconut/carry_weight(sw_type, 1)
   
    print("     To carry a 1 lb coconut you will need", math.ceil(num_sw),sw_type,"swallows\n")



# ###########################################################
# main code while loop
# - Dylan and Hunter
# ###########################################################
while True:
    #Starts the swallow shenanigans
    sw_type,swallow_num=get_swallows()
    print("\nResults for", swallow_num, sw_type, "swallows\n")
   
    #Puts Carry wieght as a variable to call
    weight=carry_weight(sw_type, swallow_num)
   
    #Gets Number of coconuts and puts it into a variable
    num_nuts=num_coconuts(weight, 453.59)
    print("    ", swallow_num, sw_type, "swallows can carry", round(weight,3), "g which is", round(num_nuts,3) , "1 lb coconuts\n")
   
    #Gives the number of swallows needed to carry a 1lb coconut
    num_swallows(sw_type,453.59)
   
    #Finishes or restarts code
    user_input = input("Would you like to try another swallow? (y/n): ")
    if user_input.lower() == "n":
        print("\nOkay fine. Ignore the swallowness.\n")
        break
    elif user_input.lower() == "y":
        print("\nSounds good. Hold onto your swallows.\n")
    else:
        print("\nYou didn't say no so im expecting you want to see more swallows.\n")




