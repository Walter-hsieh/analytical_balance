import os

files = list(filter(lambda i: ".mp4" in i, os.listdir()))

i=0

for file in files:
	filename = "video_" + str(i) + ".mp4"
	os.rename(file, filename)
	i+=1
	print(filename)



