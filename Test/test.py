data = open('a_test.txt')

a_list = []
b_list = []
for line in data:
    if 'split' in line:
        b_list.append(a_list)
        a_list = []
    else:
        el = line.strip().split(',')[-1]
        a_list.append(float(el))

b_list.append(a_list)

#print(b_list)
header_list = [0, 2, 4, 6, 8, 10, 8, 6, 4, 2, 0,]
b_list.insert(0, header_list)
#print(b_list)

string = ''
for i in range(len(b_list[0])):
    for lists in range(len(b_list)):
        string += str(b_list[lists][i]) + '\t'
    string += '\n'

stream = open('data.txt','w')
stream.write(string)
