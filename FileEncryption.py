
#make a dictionary with codes

codes = {'A': '!', 'a': '0', 'B': '@', 'b': '9', 'C': '#', 'c': '8', 'D': '$', 'd': '7', 'E': '%', 'e': '6', 'F': '^', 'f': '5', 'G': '&',
'g': '4', 'H': '*', 'h': '3', 'I': '(', 'i': '2', 'J': ')', 'j': '1', 'K': '[', 'k': '00', 'L': ']', 'l': '01', 'M': '{', 'm': '02', 'N': '}',
'n': '03', 'O': '?', 'o': '04', 'P': '/', 'p': '05', 'Q': '.', 'q': '06', 'R': ':', 'r': '07', 'S': '-', 's': '08', 'T': '=', 't': '09',
'U': '+', 'u': '10', 'V': '`', 'v': '20', 'W': '~', 'w': '30', 'X': " ' ", 'x': '40', 'Y': '|', 'y': '50', 'Z': '>', 'z': '60'}

#open/create files

infile = open('info_security.txt', 'r')
outfile = open('encrypted.txt', 'w')

#read the infile
text = infile.read()

#create for loop and write to outfile
for line in text:
    words = line.split()
    for word in words: 
        if line in codes: 
            outfile.write(codes[line])
        else:
            outfile.write(' ')


#close outfile 

outfile.close()