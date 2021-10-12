#Mad libs refer to a series of inputs that a user enters. The inputs can be anything from an adjective, a pronoun or even a verb.
#After all the inputs are entered the application takes all the data and arranges it to build a story template.

print(""" Mad Libs Generator """)
loop =1
while(loop<10):  #Loop backs to this point ones code finishes
    noun = input("Choose a noun: ")
    p_noun = input("Choose a plural noun: ")
    noun2 = input("Choose a noun: ")
    place = input("Name a place: ")
    adjective = input("Choose an adjective (Describing word): ")
    noun3 = input("Choose a noun: ")
    
    #Displays story based on the user input
    print("--------------------")
    print("Be kind to to your", noun,"-footed",p_noun)
    print("For a duck may be somebody's", noun2,",")
    print("Be kind to your",p_noun,"in",place)
    print("Where the weather is always",adjective,".")
    print()
    print("You may think that is this the",noun3,",")
    print("Well it is.")
    print("--------------------")
    
    #Loop back to "loop = 1"
    loop = loop+1
