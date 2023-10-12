#create dictionary
myDictionary = {
"'a': '65',
'b': '66',
'c': '67'
print (type (myDictionary)) print (myDictionary)
#Add item in dictionary myDictionary['d'] = '68'
myDictionary['e'] = '69'
myDictionary['f'] = '70'
print ("dictionary after adding item", myDictionary)
#length of dictionary
length = len (myDictionary)
print ('Length of dictionary is:', length)
#print key
for key in myDictionary:
print ("keys: ", key)
#print values
for key, value in myDictionary.items():
print ("values", value)
#Clear dictionary myDictionary.clear() print (myDictionary)
Intro. to Prog. with Python (MU-B.Sc. Comp.)
