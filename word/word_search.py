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


def word_search(current_word, count_sym): #поиск слова
    with open(file_name, 'r', encoding='utf8') as file:
        for line in file:
            count_char_line = 0
            for char in line:
                if(current_word[0]==char):
                    while n < count_sym:
                        if (count_char_line != len(line) - (count_sym - 1)):
                            if(check_partline(current_word, line, count_sym, count_char_line)==True):
                                line1_cur=line[count_char_line + count_sym]
                                word= str(current_word) + line1_cur
                                if (current_word not in more_letter):
                                    more_letter[current_word] ={word:1}
                                else:
                                    if(word in more_letter[current_word]):
                                        more_letter[current_word][word]+=1
                                    else:
                                        more_letter[current_word][word]=1

                count_char_line+=1

    new_word=max_char(more_letter[current_word])

    more_letter.clear()
    return new_word

more_letter={}
word_zero=input("Введите букву: ") #Вводим первую букву из, которого составится слово
word_second = word_zero+max_char(one_letter[word_zero]) #слово с двумя буквами, вторая наиболее часто встречаемая
while True:
    word_more = word_search(word2, ne)
#word_second=