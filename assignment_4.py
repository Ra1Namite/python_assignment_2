friend_names = list()
x = id(friend_names)
print('Initial list:',friend_names)

while True:
    name = input('enter name or (quit) to end: ').strip()
    if name.lower() == 'quit':
        break
    friend_names.append(name)
print('\nUpdated list:', friend_names)

y = id(friend_names)

if x == y:
    print('\nlist id has not changed')
else:
    print('\nlist id has changed')

friend_names.sort()
print('\nSorted list:', friend_names)

print('\nfirst item:', friend_names[0])
print('second item:',friend_names[1])
