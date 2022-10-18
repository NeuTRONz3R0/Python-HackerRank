#A sorted array is rotated at some unknown point, find the minimum element in
#it.

#Input: {5, 6, 1, 2, 3, 4}
#Output: 1
#__________________________________________________

import random
x = [int(x) for x in input("Enter List Elements: ").split()] #Using list comprehension for inputing list elements 
#random.shuffle(x) #shuffeling because user might enter sorted array 
print("input: ",x)
print("output: ",min(x))
