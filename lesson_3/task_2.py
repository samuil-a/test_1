def show_data(name, sur, year, city, email, phone):
    print(f'Введены данные Имя-{name}, Фамилия-{sur}, Год рождения-{year},'
          f' Город-{city}, email-{email}, телефон-{phone}')


while True:
    print('Введите данные о пользователе')
    try:
        val_name = input('Имя:')
        val_sur = input('Фамилия:')
        val_year = int(input('Год рождения:'))
        val_city = input('Город проживания:')
        val_email = input('Электронная почта:')
        val_phone = input('Номер телефона')
        show_data(name=val_name, sur=val_sur, year=val_year, city=val_city, email=val_email, phone=val_phone)
    except ValueError:
        print("Введены некорректные данные")
    if input('Выйти из программы (да - Y(y))? :') in ('y', 'Y'):
        break
