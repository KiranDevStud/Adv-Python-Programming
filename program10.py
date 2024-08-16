from functools import reduce

number=[1,2,3,4,5,6,7,8,9]
product=reduce(lambda x,y:x*y,number)
print("Product of elements is:",product)
