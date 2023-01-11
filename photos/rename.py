import os

files = list(filter(lambda i: ".jpg" in i, os.listdir()))

i=0

for file in files:
	filename = "img_" + str(i) + ".jpg"
	os.rename(file, filename)
	i+=1
	print(filename)



