file = open('numbers.txt', 'r')
count = 0
tmp_str = ''
for i_line in file:
    tmp_str = i_line.strip()
    if tmp_str != '':
        count += int(tmp_str)
file_2 = open('answer.txt', 'w')
file_2.write(str(count))
file_2.close()
file.close()



