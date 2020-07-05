def is_prime(number):
    if number > 1:
        for i in range(2, int(number/2) +1):
            if number % i== 0:
                return False
        return True       
    else:
        return False

#user_input:

n = int(input('enter number: ').strip())

#function call

print('\ncheck prime number:')
y = is_prime(n)
print(y)



            