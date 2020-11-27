string = input("Введите предложение\n>")
for num, word in enumerate(string.split(), 1):
    print(f'{num}. {word[:10]}')
