#user input
import itertools
lst = list()
while True:
    a = input('enter number in list or (quit) to end: ').strip()
    if a == 'quit':
        break
    if a.isdigit():
        a = int(a)
    else:
        a = eval(a)
    lst.append(a)

print('\nlist:',lst)

#main program
my_list = [list(i) for i in list(itertools.combinations(lst, 3)) if sum(i) == 0]

print('\nResult:')
print(my_list)

