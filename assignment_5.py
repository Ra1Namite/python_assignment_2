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
    age = int(age)
    x = (first_name, last_name, age)
    lst.append(x)

print('\nInitial list:',lst)

print('\nSorting by age....')
lst.sort(key = lambda x: x[2])
print('\nSorted list:', lst)

    