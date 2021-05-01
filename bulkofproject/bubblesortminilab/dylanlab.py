#imports
from random import randrange

#list generator
def listgen(size):
    list = []
    for i in range(0, size):
        index = randrange(65, 93)
        list.append(index)
    return list

#bubble sort
def bubblesort (list):
    final = list
    #loop for entire list
    for i in range(len(final)):
        #test list value vs the rest of the list
        for j in range(0, len(final)-1):
            #if list value is greater than next replace
            if final[j] > final[j + 1]:
                #replacement code
               final[j], final[j + 1] = final[j + 1], final[j]
    return final