#Write a python program to accept elements in the form of tuples and display their sum and average



tuple_1=[]
n=int(input("Enter the number of items in the tuple: "))
for i in range(n):
    a=int(input("Enter the element:"))
    tuple_1.append(a)
sum_of_tuple=0
for i in tuple_1:
    sum_of_tuple = sum_of_tuple+i
average=sum_of_tuple/n

print("Sum of the items in the tuple: "+str(sum_of_tuple))
print("Average of the items in the tuple: "+str(average))