#✓Write a python program to find all the pairs in the list whose sum equals to a given number



def pairs_find(nums, target_sum):
    pairs =[]
    num_set= set()
    for num in nums:
        complement =target_sum-num
        if complement in num_set:
            pairs.append((complement,num))
        num_set.add(num)
    return pairs
    

numbers = [1,2,3,4,5,6,7,8,9]
sum=10
result =pairs_find(numbers,sum)
print(result)