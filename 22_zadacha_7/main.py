sport_dict = dict()
score_to_pass,chempions_count = 0,0
prize_number = 1
file_to_write = open('second_tour.txt', 'w')
name_surname_list = []


for line in open('first_tour.txt','r'):
    clean_line = line.rstrip()
    temp_list = clean_line.split(' ')
    if len(temp_list) != 1:
        sport_dict[(temp_list[0],temp_list[1])] = int(temp_list[2])
    else:
        score_to_pass = int(temp_list[0])

for score_c in sport_dict.values():
    if score_c > score_to_pass:
        chempions_count += 1
file_to_write.write(str(chempions_count) + '\n')

while chempions_count > 0:
    for name,score in sport_dict.items():
        if score == max(sport_dict.values()) and max(sport_dict.values()) > score_to_pass:
            sport_dict[name] = 0
            chempions_count -= 1
            for words in name:
                name_surname_list.append(words)
            name_surname_list[1] = name_surname_list[1][:1]
            name = (' '.join(name_surname_list))
            file_to_write.write('{number}) {name} {score}\n'.format(number = prize_number,
                                                                    name = name,
                                                                    score = score))
            prize_number += 1
            name_surname_list = []
            
file_to_write.close()

#если нужен вывод того, что получилось
for line in open('second_tour.txt', 'r'):
    print(line,end = '')