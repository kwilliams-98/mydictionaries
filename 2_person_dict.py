person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"] #list
person["pets"] = {"dog": "Fido", "cat": "Sox"} #another dictionary...within a dictionary! 

#print out dictionary
print(person)

print(type(person['children']))
    #it may be helpful to use the 'type' function to figure out what kind of object you're working with (index or key value?)

#print a specific element from the list 
print(person["children"][1]) #we can do this because this is a list type (as seen before)

#print a specific element from the dictionary 
print(person["pets"]['cat']) #just give the dictionary the key value. can't use index values!!! 

#use a for loop to print out the names of all the children 
for line in person['children']: 
    print(line)

print(' ')

for key in person['pets']:
    #print(person[key]); this gives you a KeyError because it's looking for that key in the main dictionary. 
    print(person['pets'][key])
