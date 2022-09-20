#read the file into the program 

infile = open('sometext.txt', 'r')
#textfile = infile.read()

#create a dictionary 

mydictionary = {}


#create for loop 

for line in infile: 
    for word in line.split():
        print(word)







#close the file
infile.close()