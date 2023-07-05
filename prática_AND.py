print('Comparing numbers')
X = int(input('what is the number X?'))
Y = int(input('what is the number Y?'))

if X > 100 and Y < 100:
    print(True, f' {X} is bigger than 100 and {Y} is smaller than 100.')
else:
    print(False,'Something went wrong')