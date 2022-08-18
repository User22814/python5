# task 1 Необходимо вывести на экран названия дня недели
def task_1():
    print("*******************************************")
    print("Task 1")
    number_task1 = int(input("Введите номер дня недели (1-7): "))
    dict_task1 = {
        1: 'Понедельник',
        2: 'Вторник',
        3: 'Среда',
        4: 'Четверг',
        5: 'Пятница',
        6: 'Суббота',
        7: 'Воскресенье',
    }
    if number_task1 < 7 or number_task1 > 0:
        print(f'День недели: {dict_task1[number_task1]}')
    else:
        print("Введенное число неверное")


# task 2 Необходимо вывести на экран название месяца
def task_2():
    print("*******************************************")
    print("Task 2")
    number_task2 = int(input("Введите номер месяца (1-12): "))
    dict_task2 = {
        1: 'Январь',
        2: 'Февраль',
        3: 'Апрель',
        4: 'Март',
        5: 'Май',
        6: 'Июнь',
        7: 'Июль',
        8: 'Август',
        9: 'Сентябрь',
        10: 'Октябрь',
        11: 'Ноябрь',
        12: 'Декабрь',
    }
    if number_task2 < 12 or number_task2 > 0:
        print(f'Название месяца: {dict_task2[number_task2]}')
    else:
        print("Введенное число неверное")


# task 3 Если число больше нуля нужно вывести надпись «Number is positive»,
# если меньше нуля «Number is negative», если равно нулю «Number is equal to zero»
def task_3():
    print("*******************************************")
    print("Task 3")
    number_task3 = int(input("Введите число: "))
    if number_task3 > 0:
        print('Number is positive')
    elif number_task3 == 0:
        print("Number is equal to zero")
    else:
        print("Number is negative")


# task 4 Пользователь вводит два числа. Определить, равны
# ли эти числа, и, если нет, вывести их на экран в порядке возрастания.
def task_4():
    print("*******************************************")
    print("Task 4")
    arr_task4 = input("Введите два числа: ").split()
    arr = list(map(float, arr_task4))
    if arr[0] == arr[1]:
        print("Числа равны")
    elif arr[0] > arr[1]:
        print(f"{arr[0]} > {arr[1]}")
    elif arr[0] < arr[1]:
        print(f"{arr[0]} < {arr[1]}")


# task 5 Требуется проанализировать все
# числа в этом диапазоне по следующему правилу: если
# число кратно 7, его надо выводить на экран.
def task_5():
    print("*******************************************")
    print("Task 5")
    arr_task5 = input("Введите два числа (начало и конец диапозона): ").split()
    arr = list(map(int, arr_task5))
    for i in range(arr[0], arr[1] + 1):
        if i % 7 == 0:
            print(i)


# task 6 Требуется проанализировать все числа в этом диапазоне. Нужно вывести на экран:
# 1. Все числа диапазона;
# 2. Все числа диапазона в убывающем порядке;
# 3. Все числа, кратные 7;
# 4. Количество чисел, кратных 5.
def task_6():
    print("*******************************************")
    print("Task 6")
    arr_task5 = input("Введите два числа (начало и конец диапозона): ").split()
    arr = list(map(int, arr_task5))
    print("Все числа диапозона:")
    for i in range(arr[0], arr[1] + 1):
        print(i)

    print("\nВсе числа диапозона в убывающем порядке: ")
    for i in range(arr[1], arr[0] - 1, -1):
        print(i)

    print("\nВсе числа кратные 7: ")
    for i in range(arr[0], arr[1] + 1):
        if i % 7 == 0:
            print(i)

    print("\nКоличество чисел кратных 5: ")
    summa = 0
    for i in range(arr[0], arr[1] + 1):
        if i % 5 == 0:
            summa += 1
    print(summa)


# task 7
# 1. Если число кратно 3 (делится на 3 без остатка) нужно вывести слово Fizz.
# 2. Если число кратно 5 нужно вывести слово Buzz.
# 3. Если число кратно 3 и 5 нужно вывести Fizz Buzz.
# 4. Если число не кратно не 3 и 5 нужно вывести само число.
def task_7():
    print("*******************************************")
    print("Task 7")
    arr_task5 = input("Введите два числа (начало и конец диапозона): ").split()
    arr = list(map(int, arr_task5))
    for i in range(arr[0], arr[1] + 1):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{i}: Число кратно 3 и 5 FIZZ BUZZ")
        elif i % 3 == 0:
            print(f"{i}: Число кратно 3 FIZZ")
        elif i % 5 == 0:
            print(f"{i}: Число кратно 5 BUZZ")
        else:
            print(f"{i}")


if __name__ == '__main__':
    task_1()

    task_2()

    task_3()

    task_4()

    task_5()

    task_6()

    task_7()
