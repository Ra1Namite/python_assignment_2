#function definition
def write_csv(filename, my_list):
    import csv

    with open(filename, 'w') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(['name', 'address', 'age'])
        for i in my_list:
            csv_writer.writerow(i)


#function call

write_csv('new.txt', [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)])

