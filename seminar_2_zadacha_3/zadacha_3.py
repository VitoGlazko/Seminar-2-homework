#Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
word_1 = input("Введите первое слово: ")
word_2 = input("Введите второе слово: ")
hgnel = len(word_1)
lengh = len(word_2)
count = 0
for i in range(lengh):
    for h in range(hgnel):
        if   word_1[h] == word_2[i]:
            count = count + 1

            
