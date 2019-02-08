#!/usr/bin/env python

import os

myfilename = "housing.data.txt"

# if os.path.isfile(myfilename):
#   print("yay, I have a file")
#   if sky == blue:
#     print('yay the sky is blue')
# else:
#   print ('boo, no files for me')
new_lists = []
print('PART 1')
with open(myfilename, 'r') as file_handle:
    for line in file_handle.readlines():
        line_clean = line.replace('   ', ' ').replace('  ', ' ')
        line_clean = line_clean.strip()
        values = line_clean.split(' ')
        # print(len(values))
        # print(values)
        casted_lines = []
        for value in values:
            # for homework:
            if '.' not in value:
                print('{0} will be casted to integer'.format(type(value)))
                value = int(value)
            else:
                print('{0} will be casted to float'.format(type(value)))
                value = float(value)
            casted_lines.append(value)
            # identify what type of data each value is, and cast it
            # to the appropriate type, then print the new, properly-typed
            # list to the screen.
            # I.e. ['0.04741', '0.00', '11.930', '0', '0.5730', '6.0300', '80.80', '2.5050', '1', '273.0', '21.00', '396.90', '7.88', '11.90']
            # becomes: [0.04741, 0.0, 11.93, 0, 0.573, '6.03, 80.8, 2.505, 1, 273.0, 21.0, 396.90, 7.88, 11.90]
            # print(float(value))
        # print(values)
        print(casted_lines)

   # part 2 of homework
        new_lists.append(casted_lines)
    print('PART 2')
    num_of_cols = len(new_lists[0])
    columns =[]
    for i in range(num_of_cols):
        col_i = []
        for row in new_lists:
            col_i.append(row[i])
        columns.append(col_i)

    # display on screen
    for i in range(num_of_cols):
        # to view better, print 10 first values of each column:
        print('column {0} is {1}'.format(i+1, columns[i][0:10]))
        # print whole columns
        # print('column {0} is {1}'.format(i + 1, columns[i]))
    print('finished!')
