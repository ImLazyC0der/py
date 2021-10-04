#Program to display the Fibonacci Sequence
nterms = int(input("How many terms? "))
n1, n2 = 0, 1                                   #first number of sequence
count = 0
if nterms <= 0:                                 #To Check if the number of terms is valid
   print("Please enter a positive integer: ")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")                 #Generate fibonacci sequence
   while count < nterms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1

#By Vishwa-A-J-Rao
