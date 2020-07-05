#function definition

def convert_case(string, separator='_'):
    
    output = ''.join([separator+letter.lower() if letter.isupper()  
               else letter for letter in string]).lstrip(separator) 
    return output

#user input

n1 = input('\nenter the string (camel cased): ').strip()
n2 = input('enter separator (default = snake cased): ')

print('\nSample string: ',n1)
#function call
if n2 == '':
    y = convert_case(n1)
else:    
    y = convert_case(n1, n2)

print('\nConverted string: ',y)






    
