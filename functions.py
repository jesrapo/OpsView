'''
    File name: functions.py
    Author: Jesse Rapoport
    Date created: 10/15/2018
    Date last modified: 10/15/2018
    Python Version: 2.7.12
    Created for OpsView
'''

from Person import *

ideal_characteristics = []
#a list of all the ideal characteristics from the user

jesse = Person()
joe = Person()
#joe and jesse, the two options for an ideal candidate

def print_introduction():
    #prints the introduction to the program, and waits for a return-key press
    print('''

Hello, and welcome to the 100% objective Find An Employee program!

In this program, you will design the employee of your dreams, and then get matched with someone who's hopefully close to your ideal employee!

For this program, we ask that you have the Opsview Monitor Enterprise Plan installed on your personal computer. Because Why Not?''' + u'\u2122')

    print
    
    raw_input("Please press enter to begin! ")

    print



def get_yes_or_no_answer(prompt):
    #gets a yes/no answer from the user, and returns the answer as true/false
    
    user_response = raw_input(prompt + " (Y/n): ")
    
    print
    
    if(user_response.lower() == "y" or user_response.lower() == "yes"):
        return True

    elif(user_response.lower() == "n" or user_response.lower() == "no"):
        return False
    
    #if the user gives a non-Y/n answer, call the function again recursively
    else:
        print("Error. Your response was not a simple \"Y\" or \"n\". Please try again.\n")
        return get_yes_or_no_answer(prompt)

def save_yes_or_no_answer(prompt):
    #saves the answer to a yes/no question into the list of ideal characteristics
    
    yes_or_no = get_yes_or_no_answer(prompt)
    ideal_characteristics.append(yes_or_no)

def get_scale_answer(prompt, top_number):
    #saves the answer to a scale of 1-5 (or 1/2) question to the list of ideal characteristics
    
    #if it's just a choice of 1 or 2, change the wording slightly, tell user it's a choice
    if(top_number == 2):
        user_response = raw_input(prompt + " (1 or 2): ")
        
    #if it's actually a scale of more than 1-2, then phrase it accordingly
    else:  
        user_response = raw_input(prompt + " (1 to " + str(top_number) + "): ")

    print
    
    #if a non-number was entered, tell the user to try again
    if(not user_response.isdigit()):
        print("Error. You entered something that was not a positive integer. Please try again.\n")
        return get_scale_answer(prompt, top_number)

    #otherwise, convert the string to an int
    else:
        user_response = int(user_response)

    #if the user's response is valid, simply return it
    if(user_response >= 1 and user_response <= top_number):
        return user_response
    
    #if the user gives an answer outside of the appropriate range, call the function again recursively
    else:
        print("Error. You entered a number that was not an integer in the appropriate range. Please try again.\n")
        return get_scale_answer(prompt, top_number)
    
def save_1_or_2_answer(prompt):
    #saves 2-option question answer into the list of ideal characteristics

    one_or_two = get_scale_answer(prompt, 2)
    ideal_characteristics.append(one_or_two)

def save_scale_answer(prompt):
    #saves scale of 1-5 question answer into the list of ideal characteristics
    scale_number = get_scale_answer(prompt, 5)
    ideal_characteristics.append(scale_number)

def initialize_jesse_and_joe():
    #wrapper function to initialize Person's Jesse and Joe
    initialize_jesse(jesse)
    initialize_joe(joe)

def initialize_jesse(jesse):
    #initializes the Person Jesse with his characteristics
    
    jesse.set_name("Jesse Rapoport")
    jesse.set_characteristics([True, True, False, 1, 2, 1, 1, 3, 5, 5])
    jesse.set_description('''Jesse Rapoport is a young, flexible programmer who finds true joy and passion 
in what he does. He is passionate about life, passionate about mathematics,
passionate about working hard, and passionate about programming. He finds his 
greatest joys in learning, and so software development seems to be the perfect field
for him. He documents his code (somewhat) well, he is receptive to feedback, he is flexible, and
he is constantly learning. He brings a zest with him everywhere he goes, and he helps 
make the workplace a more fun and exciting atmosphere, all the while working hard, 
often going above and beyond for no recognition other than his own. He drinks his coffee 
black, and he has a generally great style.

He can be reached at jessehrapoport@gmail.com, or at (503) 820-1358.''')


def initialize_joe(joe):
    #initializes the Person Joe with his characteristics

    joe.set_name("Joe Shmoe")
    joe.set_characteristics([False, False, True, 2, 1, 2, 2, 1, 1, 1])
    joe.set_description('''Joe Shmoe went to the University of Oregon for computer science, but was not particularly interested in it. 
He does not enjoy programming, and does the bare minimum of everything he\'s asked to do. 
His code technically runs, but in less common situations it quickly breaks down, and when it 
comes to fixing the code, it is so poorly documented and convoluted to the point where all 
of his coworkers dread working with him. He also has a strong disdain for anything containing chocolate.

His phone number and e-mail address are coming soon!''')

def ask_questions():
    #asks the user questions, and saves her answers into a list    

    save_yes_or_no_answer("Does your ideal employee have a keen attention to detail?")

    save_yes_or_no_answer("Does your ideal employee highly value good communication?")

    save_yes_or_no_answer("Does your ideal employee hate all chocolate?")

    save_1_or_2_answer("Does your ideal employee 1. enjoy programming, or 2. only program for that cold, hard cash?")

    save_1_or_2_answer("Does your ideal employee 1. have all personal skills centered around programming, or 2. have passions and talents outside of the programming world?")
    
    save_1_or_2_answer("Does your ideal employee 1. have leadership experience, or 2. only know how to follow?")
    
    save_1_or_2_answer("Is your ideal employee 1. flexible and easy-going, or 2. rigid and easily frustrated?")
    
    save_scale_answer("How much does your ideal employee ask questions? (Where 1 is to never ask, 5 is to never Google, and 3 is a happy middle) ")

    save_scale_answer("How curious is your ideal employee?")

    save_scale_answer("How passionate is your ideal employee about programming, and about learning in general?")

    #print (ideal_characteristics)
    #this can be used to easily copy and paste an employee's preferences when creating new employees in the code

def compare_ideal_to_jesse_and_joe():
    
    #compares the user's answers to jesse and joe's characteristics, and determines the winner
    jesse.compare_characteristics(ideal_characteristics)
    joe.compare_characteristics(ideal_characteristics)

    raw_input("Please press enter to see the results! ")

    print

    if(jesse.similarity == joe.similarity):
        announce_tie()

    elif(jesse.similarity > joe.similarity):
        announce_who_won(jesse, joe)

    else:
        announce_who_won(joe, jesse)

def announce_tie():
    #announces a tie if there is one
    
    print ("Aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaand it's a tie!! With a similarity of " + str(runner_up.similarity) + "% to your ideal employee." )
    print
    print ("However, we at Generic Programming Indrustries" + u'\u2122' + "have good news:")
    print
    print ("Although he does not meet your taste, we have the #1 most qualified person on this side of the Mississippi.")
    print
    raw_input ("His name is... Drum roll please... (Please press enter) ")
    print
    print ("Jesse Rapoport!!!")
    print
    raw_input("Please press enter to see a quick biography of the (kind-of) winner.")
    print
    print (jesse.description)
        

def announce_who_won(winner, runner_up):
    #announces the runner-up, the winner, and describes the latter
    
    print ("Aaaaand the runner up is.......... " + runner_up.name + "! With a similarity of " + str(runner_up.similarity) + "% to your ideal employee. ")
    print
    raw_input ("Please press enter to continue.")
    print
    raw_input ("And, the winner, of the 2018 Find Your Ideal Employee contest is......(please press enter...)")
    print
    raw_input ("Drum roll please.............. (Please press enter and do an actual drum roll on your desk)")
    print
    print (winner.name + "!!!!!!!!! With a similarity of " + str(winner.similarity) + "% to your ideal employee!")
    print
    raw_input("Please press enter to read a short biography of your winner, " + winner.name + ". ")
    print
    print (winner.description)
    print

def exit_program():
    #thanks the user for using the program, and exits
    raw_input ("Please press enter to exit the program. ")
    print
    print ("Thank you very much for using this program!")
    print
