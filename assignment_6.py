lst = list()

while True:
    name = input('enter name or (quit) to end: ').strip()
    if name.lower() == 'quit':
        break
    lst.append(name)
print('\nName list:',lst)

print('\nSearching for "John" in list...')
if 'John' in lst:
    print('\nfound')
else:
    print('\nnot found')

