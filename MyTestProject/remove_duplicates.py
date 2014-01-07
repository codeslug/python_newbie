'''
Created on Jan 7, 2014

@author: codeslug

Written for codeacedmoy exercise. 

Object: write a function which takes a single list as input, and returns a copy of that list with 
duplicate entries removed.   
'''

def remove_duplicates(my_list):    
    new_list = []
    if len(my_list) != 0: # error handling empty lists
        new_list.append(my_list[0]) # initializes first item, for debugging reasons. unless list is empty
        for count in range(len(my_list)):
            for inner in range(len(new_list)):
                if (my_list[count] == new_list[inner]):
                    break # match found, no copy to be made
                elif (inner == len(new_list)-1):
                    new_list.append(my_list[count]) # reached end of new_list with no matches -> add to new_list
    return new_list

things_i_like = ["snails", "cellos", "slugs", "the night", "slugs", "cellos", "bikes"]

print "my_list =", things_i_like
print "new_list =", remove_duplicates(things_i_like)

# my plan - 
# 1. cycle through list 1.
#     2. for each item of list 1, cycle through list 2. 
#         3. if the list 1 item does not have a match, add it to the end of list 2.
#         4. if there is a match found, stop cycling through list 2.