class ValidateParenthese:
    def valid_parenthese(self, string):
        my_list = list()
        my_dict = {'(': ')', '{': '}', '[': ']'}
        
        for x in string:
            if x in my_dict:
                my_list.append(x)
            
            elif len(my_list) == 0 or my_dict[my_list.pop()] != x:
                return False
        return len(my_list) == 0

validate = ValidateParenthese()

string = input('\nenter the string of parentheses: ').strip()
print(f'\nString "{string}" valid?')
print(validate.valid_parenthese(string))





