#function definition

def binary_search(lst, item):
    start = 0
    end = len(lst) - 1 
    
    
    while start <= end:
        
        mid = (start + end)//2
        if lst[mid] == item:
            return mid
        else:
            if item > lst[mid]:
                start = mid + 1
            else:
                end = mid - 1
    return -1            

# user input

my_list = list()
while True:
    print('enter item in list and (quit) to stop: ')
    n = input().strip()
    if n == 'quit':
        break
    if n.isdigit():
        n = int(n)
    my_list.append(n)
print('\nSequence:',my_list)
my_list.sort()
print('\nsorted sequence:',my_list)
n1 = input('\nenter item to be searched: ').strip()
if n1.isdigit():
    n1 = int(n1)

#function call
x = binary_search(my_list, n1)

print('\nResult:',x)

