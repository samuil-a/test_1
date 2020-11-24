def int_func(word):
    for i in word:
        if ord('a') > ord(i) or ord(i) > ord('z'):
            print(f'Слово {word} не соответствует требованиям, быть написаной только маленькими латинскими буквами')
            return
    if not word.isalpha() or not word.islower():
        print(f'Слово {word} не соответствует требованиям, быть написаной только маленькими латинскими буквами')
        return
    return word.title()


print(int_func(input('Введите слово строчными латинскими буквами:')))

val = input('Введите предложение строчными латинскими буквами:')
words = val.split()
for num, j in enumerate(words):
    tmp = int_func(j)
    if type(tmp) != type(j):
        print(f'Выполнение программы прервано ')
        break
    words[num] = tmp
else:
    print(' '.join(words))
