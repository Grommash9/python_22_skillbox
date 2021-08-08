#Note that since there is a current directory for each drive, os.path.join("c:", "foo") represents a path relative to the current directory on drive C: (c:foo), not c:\foo.

import os

def file_writter(path,text):
    temp_file = open(path,'w')
    temp_file.write(text)
    temp_file.close()
    print('Файл сохранен в',path)
    
def save_text_to_file(text):
    path_names_list = input('Куда хотите сохранить документ? Введите последовательность папок (через пробел):').split(' ')
    real_path = os.path.join(*path_names_list)
    if os.path.exists(real_path):
        file_path = os.path.join(real_path,(input('Введите имя файла: ') + '.txt'))
        if os.path.exists(file_path):
            choose = input('Вы действительно хотите перезаписать файл?(да/нет)')
            if choose in positive_answers:
                file_writter(file_path,text)
            else:
                print('Файл не будет перезаписан')
        else:
            file_writter(file_path,text)
    else:
        print('Такой каталог не обнаружен, пожалуйста попробуйте ещё')
    
text = input('Введите строку: ')
positive_answers = ['да', 'lf','Да','ДА','дА','Lf','fL','LF']

save_text_to_file(text)