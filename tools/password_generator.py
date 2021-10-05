import  random

#A function to shuffle all the characters of a string
def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)

#Main program starts here
uppercaseLetter1 = chr(random.randint(65,90)) #Generate a random upper case ltter based on ASCII code
uppercaseLetter2 = chr(random.randint(65,90))

lowercaseLetter1 = chr(random.randint(97,122))
lowercaseLetter2 = chr(random.randint(97,122))

digit1 = chr(random.randint(48,57)) 
digit2 = chr(random.randint(48,57))

punctuationSign1 = chr(random.randint(33,38)) #Generates random special character !"#$%&
punctuationSign2 = chr(random.randint(33,38))

password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + digit1 + digit2 + punctuationSign1 + punctuationSign2
password = shuffle(password)

#ouput
print("Generated password is: "+password)