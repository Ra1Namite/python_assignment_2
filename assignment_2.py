year = int(input('enter the year: ').strip())  #user input


x = 'a leap year'
y = 'not a leap year'
z = f"{year} is"


if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(z,x)
        else:
            print(z,y)
    else:
        print(z,x)

else:
    print(z,y)


        
        