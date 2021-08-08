import os

results_list = [0,0,0]

def file_finder(path,results_list):
    for i_elem in os.listdir(path):
        real_path = os.path.join(path,i_elem)
        if os.path.isdir(real_path):
            results_list[0] += 1
            file_finder(real_path,results_list)
        else:
            results_list[1] += 1
            size = os.stat(real_path)
            results_list[2] += size[6]

#'C:\PerfLogs'
while True:
    target_path = input('Путь до каталога: ')
    if os.path.exists(target_path):
        break
    else:
        print('Такая директория не обнаружена, попробуйте ещё раз')

file_finder(target_path,results_list)


print('Количество подкаталогов:',results_list[0],'\nКоличество файлов:',results_list[1],'\nРазмер каталога (в Кб)',results_list[2] / 1024)