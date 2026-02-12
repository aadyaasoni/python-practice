# Write a program that takes 5 numbers as input from the user and stores them in a list. Then, find the maximum and minimum numbers in the list and count how many of the numbers are even.
list1 =[]
count=0
for i in range(5):
    num=(int(input("enter an number")))
    list1.append(num)
    if i == 0:
        max_num = num
        min_num = num
    if max_num<num:
        max_num=num
    if min_num>num:
         min_num=num
    if num%2==0:
        count=count+1
print(list1)
print(max_num)
print(min_num)
print(count)
