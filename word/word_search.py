def max_char(keys): #Ищет максимально встречаемый символ
    max_count=0 #максимальный в данный момент
    max_char= ''
    slash='\\n'
    for key in keys:
        if((keys[key])>max_count and key!=slash): #поиск максимального

            max_count=keys[key]
            max_char=key
    max_char=fr'{max_char}'
    return max_char
def check_partline(current_word, current_line, ne, count): #Проверка, подходит ли линия
    n=1
    len_line=len(current_line)
    isDesiredText=True #bool, подходит ли часть текста моему тексту
    while n<=ne-1:
        count1=count+n<len_line-1
        count2=len(current_word)
        if((count1 and n<count2+1)==True):
            line2=current_line[count + n - 1]
            w=current_word[n - 1]
            if(line2!=w):
                isDesiredText=False
        else: isDesiredText=False
        n += 1
    return isDesiredText
def word_search(current_word, count_sym): #поиск слова
    with open(file_name, 'r', encoding='utf8') as file:
        for line in file:
            count_char_line = 0
            for char in line:
                n=1
                if(current_word[0]==char):
                    while n < count_sym:
                        n += 1
                        if (count_char_line != len(line) - (count_sym - 1)):
                            if(check_partline(current_word, line, count_sym, count_char_line)==True):
                                line1_cur=line[count_char_line + count_sym]
                                if(line1_cur!='\n'):
                                    word= str(current_word) + line1_cur
                                    if (current_word not in more_letter):
                                        more_letter[current_word] ={word:1}
                                    else:
                                        if(word in more_letter[current_word]):
                                            more_letter[current_word][word]+=1
                                        else:
                                            more_letter[current_word][word]=1
                                else:
                                    break

                count_char_line+=1
    if(current_word in more_letter):
        new_word=max_char(more_letter[current_word])
    else: new_word=current_word
    more_letter.clear()
    return new_word
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
count_sym=2
more_letter={}
word_zero=input("Введите букву: ") #Вводим первую букву из, которого составится слово
word_second = word_zero+max_char(one_letter[word_zero]) #слово с двумя буквами, вторая наиболее часто встречаемая
while True:
    word_more = word_search(word_second, count_sym)
    word_second=word_more
    if (count_sym >= len(word_more)):
        break
    len_word = len(word_more) - 1
    slash=r'\\'
    if (word_more[len_word] == ' ' or word_more[len_word]==slash):
        word_True = False
        print('break')
        break
    count_sym+=1
print(word_second)
