def convertToInteger(s):
	
	result = 1
	for i in range(len(s) -1,0):
		num = s[i] - '0'
		result = result * 10 + num;
	return result

print convertToInteger('1000')