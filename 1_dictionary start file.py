import random

phonebook = {'Chris':'555−1111',
             'Katie':'555−2222',
             'Joanne':'555−3333'}



print()
print('*****  start section 1 - print dictionary ********')
print()

print(phonebook)
print(type(phonebook)) #allows you to know what kind of object you are dealing with (important since python is an object-oriented language)
print(phonebook['Chris'])
#phone = phonebook['Chris']
#print(phone)

mydictionary = {}
print(mydictionary)

mydictionary = dict(m=8,n=9) #same as the 'list' function
print(mydictionary)


print()
print('*****  end section 1 ********')
print()





print()
print('*****  start section 2 - search dictionary ********')
print()

name = 'Chris'

if name in phonebook:
    print(phonebook[name])
else: 
    print(name, 'is not in the phonebook')



print()
print('*****  end section 2 ********')
print()







print()
print('*****  start section 3 - edit/append dictionary ********')
print()

print(phonebook)
phonebook['Chris'] = '555-0123'#changing Chris's phone number. values can be updated, KEYS CANNOT (so they are immutable)
phonebook['Joe'] = '555-4444'#adding Joe to the dictionary. adds value if it does not exist
print(phonebook)


print()
print('*****  end section 3 ********')
print()






print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()

#del phonebook['Chris'] ###keyword; you will get an error if the key is not found!
#print(phonebook)


print()
print('*****  end section 4 ********')
print()






print()
print('*****  start section 5 - iterate through keys, values, items ********')
print()


for k in phonebook: #default iteration for dictionaries is keys when you do a 'for' loop!
    print(k) #key is not a reserved word, just a variable (call it anything you want)
    print(phonebook[k]) 

#if you wanted to go through values instead of keys...

for value in phonebook.values(): #must call the values method if you don't want to iterate through keys. there is also a keys method (pointless)
    print(value)

for k,value in phonebook.items():
    print('Key:', k, ' Value:', value)

for tuple in phonebook.items():
    print(tuple)

print()
print('*****  end section 5 ********')
print()





print()
print('*****  start section 6 - using get and clear ********')
print()

phone = phonebook.get('Chris', 'key not found')
print(phone)

#phonebook.clear() #doesn't delete your dictionary, but clears everything out of it
#print(phonebook)

print()
print('*****  end section 6 ********')
print()

'''

print()
print('*****  start section 7 - using pop method ********')
print()






print()
print('*****  end section 7 ********')
print()



print()
print('*****  start section 8 - using popitem ********')
print()






print()
print('*****  end section 8 ********')
print()



print()
print('*****  start section 9 - using random and converting to list ********')
print()





print()
print('*****  end section 9 ********')
print()


'''





