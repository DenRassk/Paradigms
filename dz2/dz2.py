# На вход подается число n. Написать скрипт в любой парадигме,
# который выводит на экран таблицу умножения всех чисел от 1 до n.
# Обоснуйте выбор парадигм.


def muiltiplication_table(n):
    for i in range(1, n+1):
        print('\n'.join([f'{i} \t* \t{num} \t= \t{num*i}' for num in range(1, n+1)]))
        print('------------------')


print('Вывод таблицы умножения')
n = int(input('Введите натуральное число от 1 до 15: '))
muiltiplication_table(n)
