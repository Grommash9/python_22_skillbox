summa = 0

print('Содержимое файла numbers.txt')
for line in open('numbers.txt', 'r'):
    print(line,end = '')
    for symbol in line:
        if symbol.isdigit():
            summa += int(symbol)

result = open('answer.txt', 'w')
result.write(str(summa))
result.close()

print('\nСодержимое файла answer.txt')
for line in open('answer.txt', 'r'):
    print(line)
