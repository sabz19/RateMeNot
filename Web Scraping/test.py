string = "a href = askaskas >"
index1 = string.find("bloooo")
index2 = string.find(">",index1)
print index1
print index2

rs = string[index1 + 1:3]	
print rs