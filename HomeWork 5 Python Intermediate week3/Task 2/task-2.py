#task 2

from word_utils import clean, words_list, long

stroke = "Некоторая строка, строка которая содержит знаки припинания! ()-[]{};?@#$%:'\,./^&amp;*_"

#очистить предложение от знаков препинания
print(clean(stroke))
#получить список слов из предложения
print(words_list(stroke))
#получить самое длинное слово в предложении
print(long(stroke))