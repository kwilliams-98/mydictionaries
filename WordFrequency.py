
#read the file into the program 

infile = open('sometext.txt', 'r')

#create a dictionary 

mydictionary = {}


#create for loop 

for line in infile: 
    words = line.split()

    for word in words: 
        if word in mydictionary: 
            mydictionary[word] = mydictionary[word] + 1
        else: 
            mydictionary[word] = 1  

for key in list(mydictionary.keys()):
    print(key, ':', mydictionary[key])



#close the file
infile.close()