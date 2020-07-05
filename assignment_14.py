def read_csv(filename):
    import csv

    with open(filename) as f:
        csv_reader = csv.reader(f)
        my_list = list()
        
        lst = list(csv_reader)

        for row in lst[1:]:
            my_dict = dict()
            for i in range(len(row)):
                if row[i].isdigit():
                    row[i] = int(row[i])
                my_dict[lst[0][i]] = row[i]
            my_list.append(my_dict)
    return my_list


print(read_csv('new.csv'))

            


            

            


            
