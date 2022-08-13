#Given an array of integers, find the sum of its elements.
#Input Format
#The first line contains an integer,n, denoting the size of the array.
#The second line contains n space-separated integers representing the array's elements.
#_________________________________________________________________________________________________________________________________________________

n = int(input( ))
l1 = [int(i) for i in input().split(" ", n-1)]
print(sum(l1))
