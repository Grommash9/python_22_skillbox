word_list = []
frequency_dict = dict()
lines_count,letters_count,words_count = 0,0,0

for line in open('zen.txt', 'r'):
    word_list.append(line.split(' '))

for words_lists in word_list:
    lines_count += 1
    for words in words_lists:
        new_word = True
        for letter in words:
            if letter.isalpha():
                if new_word:
                    words_count += 1
                    new_word = False
                letters_count += 1
                if letter in frequency_dict:
                    frequency_dict[letter] += 1
                else:
                    frequency_dict[letter] = 1

print('Количество слов в тексте:',words_count,'\nКоличество букв в тексте:',letters_count,'\nКоличество строк в тексте:',lines_count)

minimal_frequency = min(frequency_dict.values())

print('Вот буквы, который встречаються в тексте только',minimal_frequency,'раз: ', end = '')
for keys,values in frequency_dict.items():
    if values == minimal_frequency:
        print(keys, end = ' ')