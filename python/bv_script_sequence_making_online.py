# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 14:48:07 2020

@author: Bas Vegt

Purpose: creating text file containing number 1-4 to feed into another programm

Requirements: 

Alpha: We need 960 steps, 240 sequence, every sequence 40 times.
	Alpha note one: Each need to appear 39 times in the randomized list. That list can then be appended to a list starting with ABCDEF.
Bravo: Repeat sequences not allowed.
Charlie: Repeat numbers not allowed:
Delta: Sequences are originally defined as: 
	A = 2 3 1 2
	B = 3 1 2 1
	C = 4 2 1 2
	D = 1 2 1 4
	E = 1 4 2 3
	F = 4 2 3 1
		Delta note one: This can/will be rotated later, when we insert numbers to replace the letters.#
		Delta note two: we use 1-4 here, while the related data / program sometimes uses 0-3. Be sure to check which input range your program expects and change the values of a-f accordingly.
Echo: From Charlie & Delta it follows that the following restrictions apply in follow-ups:
	A: May not be followed by A.
	B: May not be followed by B, D and E
	C: May not be followed by C and A
	D: May not be followed by D, C and F
	E: May not be followed by E and B
	F: May not be followed by F, D and E
"""

import random, copy, sys, os

dir_name = 'TestSeqs' # The folder to write in
file_name = 'TestSeqOnline' # desired name for the txts, appended by the number
files = 80 # input the number of sequences to be created (excl 0)
words = [
[4, 1, 2, 4],
[1, 2, 4, 2],
[3, 4, 2, 4],
[2, 4, 2, 3],
[2, 3, 4, 1],
[3, 4, 1, 2],
]

# Defining the function:
def create_array(length, previous_end = ''):
    # Defining initial list of options:
    items_initial = []
    for i in range(length):
        items_initial.extend(words)
    # /Defined initial list of options.
    
    items_shuffled = [] # Create empty list for output
    while len(items_shuffled) < length*6: # Untill we reach the desired size:
        'Attempting array composition.'
        items_remaining = copy.deepcopy(items_initial) # Pull the initial items
        items_shuffled = [] # Create empty list for output
        item_previous = previous_end # Create empty string to record each previous step
        while items_remaining: # As long as items_remaining isn't empty:
            items_possible = items_remaining # take the list of currently remaining items
            if item_previous: # if there is a previous item (i.e. after step 1) 
                # filter for viable options (specific filter dependent on the moves (numbers) in each sequence (letter))
                items_possible = [x for x in items_possible if x != item_previous and x[0]!= item_previous[3]]
            if not items_possible: # if list of viable options (after the filter) is now empty:
                print('No valid solution. Trying again...') #Tell me.
                break # Give up and try at the top.
            item_new = random.choice(items_possible) # Choose any of the remaining items
            items_shuffled.append(item_new) # append that item to our items_shuffled list
            items_remaining.remove(item_new) # remove that item from our remaining options 
            item_previous = item_new # note the item as the now previous item
    if not items_remaining: # if there are no more items remaining at all:
        print('Valid order found.') # tell me
    for itemno in range(len(items_shuffled)):
        item = items_shuffled[itemno]
        if item == [4, 1, 2, 4]:
            replacement = '0'
        elif item == [1, 2, 4, 2]:
            replacement = '1'       
        elif item == [3, 4, 2, 4]:
            replacement = '2'
        elif item == [2, 4, 2, 3]:
            replacement = '3'
        elif item == [2, 3, 4, 1]:
            replacement = '4'
        elif item == [3, 4, 1, 2]:
            replacement = '5'
        else: 
            print('error')
            break
#        items_shuffled[itemno] = (''.join(str(item)))
        items_shuffled[itemno] = replacement
    return items_shuffled, item_previous
#/ Defined a function
    


if os.path.exists(os.path.join(os.curdir, dir_name, file_name + str(int) + '.txt')): #  if file with name pre-exists if file with name pre-exists
    print('Aborting: File already exists.') 
    sys.exit() # Safety measure: abort.
else:
    outfile = open(os.path.join(os.curdir, dir_name, file_name + '.txt'), 'w')
    outfile.write('\t\t')
    for int in range(1,files+1):
        print('Acknowledged: Writing seq ' + str(int) + '. Standby.')        
        wordSeq1, last = create_array(1)
        extension, last = create_array(9, last)
        wordSeq1.extend(extension)
        wordSeq2, last = create_array(10, last)
        wordSeq3, last = create_array(10, last)
        wordSeq4, last = create_array(10, last)
        outfile.write('if(participantID === ' + str(int) + '){\n\t\t\twordSeq1 = [' + (','.join(wordSeq1)) + '];\n\t\t\twordSeq2 = [' + (','.join(wordSeq2)) + '];\n\t\t\twordSeq3 = [' + (','.join(wordSeq3)) + '];\n\t\t\twordSeq4 = [' + (','.join(wordSeq4)) + '];\n\t\t}\n\t\telse ')
    print('All done. File should be found at ' + os.path.join(os.curdir, dir_name, (file_name+'.txt')))
    outfile.close()