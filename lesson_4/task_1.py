from sys import argv

if len(argv) == 4:
    name, hors, salary, bonus = argv
    print(f'Расчет зарплаты ({argv[1]}*{argv[2]})+{argv[3]}={int(hors)*int(salary)+int(bonus)}')
