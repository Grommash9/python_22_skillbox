file = open('zen.txt','r')
lines_list = file.readlines()
lines_list.reverse()
print(''.join(lines_list))


# Первое что пришло в голову
# lines_in_file = 0
# current_line = 0
#
# for line in open('zen.txt','r'):
#     lines_in_file += 1
#
# for iteration_number in range (lines_in_file):
#     for line in open('zen.txt','r'):
#         current_line += 1
#         if lines_in_file == current_line:
#             print(line,end = '')
#             lines_in_file -= 1
#             current_line = 0
#             break