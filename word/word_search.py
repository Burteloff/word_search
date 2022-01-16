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
def max_char(keys): #Ищет максимально встречаемый символ
    max_count=0 #максимальный в данный момент
    max_char= ''
    for key in keys:
        if((keys[key])>max_count): #поиск максимального
            max_count=keys[key]
            max_char=key
    return max_char
word_zero=input("Введите букву: ") #Вводим первую букву из, которого составится слово
word_second = word_zero+max_char(one_letter[word_zero]) #слово с двумя буквами, вторая наиболее часто встречаемая
while True:

#word_second=