def number_sequence(x, y):
    current = x
    while current <= y:
        yield current
        current += 1
        
for number in number_sequence(5, 10):
    print(number)
