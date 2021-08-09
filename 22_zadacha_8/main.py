english_alphabet_lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
total_letters_count = 0
freq_dict = dict()
file_to_write = open('analysis.txt', 'w')

def file_writter(any_list):
    while len(any_list) > 0:
        minimal_letter_index = 35
        for mini_lists in any_list:
            if english_alphabet_lower.index(mini_lists[0]) < minimal_letter_index:
                minimal_letter_index = english_alphabet_lower.index(mini_lists[0])
                hightest_letter_index = any_list.index(mini_lists)       
        file_to_write.write(str(any_list[hightest_letter_index][0]) + ' ' + str(any_list[hightest_letter_index][1]) + '\n')
        print(any_list[hightest_letter_index])
        any_list.remove(any_list[hightest_letter_index])

for line in open('text.txt'):
    for letter in line:
        if letter.isalpha():
            total_letters_count += 1
            if letter in freq_dict:
                freq_dict[letter.lower()] += 1
            else:
                freq_dict[letter.lower()] = 1
            
for letter,frequency in freq_dict.items():
    freq_dict[letter] = round(frequency / total_letters_count, 3)

while max(freq_dict.values()) > 0:
    temp_list = []
    local_max = max(freq_dict.values())
    for letters,quantity in freq_dict.items():
        if quantity == local_max:
            temp_list.append([letters,quantity])
            freq_dict[letters] = 0
    file_writter(temp_list)
    

file_to_write.close()