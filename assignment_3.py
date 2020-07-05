string = input('enter text: ').strip()

lst1 = list(dict.fromkeys(string.split()))
my_list = list()

for x in lst1:
    anagram_list = list()
    anagram_list.append(x)
    for y in lst1:
        if len(x) == len(y):
            if y != x and (sorted(x) == sorted(y)):
                anagram_list.append(y)
        
    if len(anagram_list) > 1:
        my_list.append(anagram_list)       

#removing duplicate anagram lists
my_list = [tuple(sorted(item)) for item in my_list ]

my_list = [list(x) for x in dict.fromkeys(my_list)]
print('\nList of anagrams:')
print(my_list)


    

