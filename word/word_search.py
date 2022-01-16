file_name=input("Введите название файла Пример: text.txt\n") #название файла
one_letter={} #словарь из, которого вытягиваем одну букву и последующую за ним
prev_char='' #первый символ для поиска в словаре
with open(file_name,'r',encoding='utf8') as file: #открываем файлик и добавляем символ + символ последующий за ним в словарь stat
    for line in file:
        for char in line:
            if prev_char in one_letter:
                if char in one_letter[prev_char]:
                    one_letter[prev_char][char]+=1
                else:
                    one_letter[prev_char][char]=1
            else:
                one_letter[prev_char]={char:1}
            prev_char=char
stats2={}