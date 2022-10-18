#Given two strings str1 and str2 and below operations that can
#performed on str1. Find minimum number of edits (operations) required to
#convert ‘str1′ into ‘str2′.
#Input :
#Str1= week
#Str2= weak
#Output: 1
#As week can be changed to weak by replacing e with a
#____________________________________________________________________________________

def MinEdit(str1, str2):
	
	len1 = len(str1)
	len2 = len(str2)

	pa = [[0 for i in range(len1 + 1)] # Create a pa array to store the previous results 
			for j in range(2)];

	for i in range(0, len1 + 1):  # remove all characters when second String 
		pa[0][i] = i

	# Start filling the pa
	for i in range(1, len2 + 1): # The loop will run for every character in second String
		for j in range(0, len1 + 1):   # This loop will compares the char from second String with first String characters
			if (j == 0):   	# If first String is empty then we have to perform add character operation to get second String
				pa[i % 2][j] = i	# here i % 2 is for bound the row number.
			elif(str1[j - 1] == str2[i-1]):
				pa[i % 2][j] = pa[(i - 1) % 2][j - 1]
			else:
				pa[i % 2][j] = (1 + min(pa[(i - 1) % 2][j],
									min(pa[i % 2][j - 1],
								pa[(i - 1) % 2][j - 1])))

	print(pa[len2 % 2][len1], "")   # if the len2 is even then we end up in the 0th row else we end up in the 1th row so we take len2 % 2 to get row

# Driver code
if __name__ == '__main__':
	
	str1 = "quantom"
	str2 = "quantum"
	
	MinEdit(str1, str2)

