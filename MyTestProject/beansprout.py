'''
Created on Dec 30, 2013

@author: codeslug

Written for codeacademy exercise.

Instructions:
Build your for/else statement in the editor. Execution of the else branch is optional, 
but your code should print a string of your choice to the editor regardless.
'''
slug_foods = ["sweet potatoes", "beansprout", "basil", "lettuce", "green peppers"]

for count in slug_foods:
    print "Do you think slugs like to eat " +count + "?"
    answer = raw_input()
    if (count != "beansprout") and (answer == "yes"):
        print "Correct, slugs like to eat " +count +"."
    elif (count != "beansprout") and (answer == "no"):
        print "Actually, slugs really enjoy eating " +count +"."
    elif (count == "beansprout") and (answer == "yes"):
        print "Surprisingly, slugs do not really like " +count +" all that much."
    else:
        print "Correct, slugs do not really like " +count +"!"
else:
    print "So there you have it! Food slugs like to eat."
    

"""
Further development:

Choose from a list of randomly assigned answers, generated in a function ie slugs_like() and slugs_dislike().

Debug yes/no response for faulty answers.

Ask "have you ever fed your slugs X" and store the responses.
Ask "did your slugs enjoy X" and store.

Generate facts to be randomly inserted into the loop.

Switch the slug_foods list to a dictionary, with the food name being a key, and the value being like/dislike/depends.
This will scale better and allow for fast changes of the slugs' fav foods.

"""