# using sep to print in new line in print statement
print ("Name:Aadyaa", "Age:19", "Course: Btech ", sep="|")

# using end to print in same line in print statement
print("Hello",end=" ")
print("World!")

#output :1-2-3-4-5
print(1,2,3,4,5,sep="-") #or "1","2","3","4","5"

#input an string and print with welcome
name=input("Enter your name:").upper()
print(f"Welcome, {name}")

#take a word from user and print first character of the word and length of word
word=input("Enter a word:")
print("First character:",word[0])
print("Length of the word:",len(word))
print("Last character :",word[-1]) 

#take 2 inputs first_name and last_name 
first_name=input("Enter your first name:").title()
last_name=input("Enter your last name:").title()
print(first_name[0] +"."+last_name[0])
