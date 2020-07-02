lst = list()
while True:
    print('\nenter required data or (quit) to end:\n')
    first_name = input('enter first name: ').strip()
    if first_name.lower() == 'quit':
        break
    last_name = input('enter last name: ').strip()
    if last_name.lower() == 'quit':
        break
    age = input('enter age: ').strip()
    if age.lower() == 'quit':
        break
    if age == '':
        age = None
    else:
        age = int(age)

    x = (first_name, last_name, age)
    lst.append(x)

print('\nInitial list:',lst)

lst1 = [v for i,v in enumerate(lst) if v[2] != None]
lst2 = [v[2] for v in lst1]

average_age = sum(lst2)/len(lst2)
print(f'\naverage age is {average_age}\n')

for x in lst1:
    if x[2] > average_age:
        print(f'{x[0]} {x[1]}: old')
    else:
        print(f'{x[0]} {x[1]}: young')
     
