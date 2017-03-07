f = open("countries.txt", "r")
list1 = []
for line in f:
	list1.append(line.strip())
	(country, rank) = line.split(",")
	print("country = " + country + "rank = " + rank) 
f.close()
