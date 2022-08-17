# task 1 Необходимо найти сумму чисел, произведение чисел
def task_1():
    print("*******************************************")
    print("Task 1")
    arr_task1 = input("Введите три числа, разделенных пробелом: ").split()
    arr = list(map(int, arr_task1))
    print(f'Сумма = {arr[0] + arr[1] + arr[2]}')
    print(f"Произведение = {arr[0] * arr[1] * arr[2]}\n")


# task 2 Необходимо вывести на экран сумму, которая останется у пользователя после всех выплат.
def task_2():
    print("\n*******************************************")
    print("Task 2")
    arr_task2 = input("Введите три числа: Зарплата за месяц, Сумма месячного платежа по кредиту в банке, "
                      "Задолженность за коммунальные услуги: ").split()
    arr = list(map(int, arr_task2))
    print(f'Оставшаяся сумма после выплат = {arr[0] - arr[1] - arr[2]}\n')


# task 3 Напишите программу, вычисляющую площадь ромба
def task_3():
    print("\n*******************************************")
    print("Task 3")
    arr_task3 = input("Введите длину двух диагоналей ромба: ").split()
    arr = list(map(int, arr_task3))
    print(f'Площадь ромба = {0.5 * arr[0] * arr[1]}\n')


# task 4 Выведите на экран надпись To be or not to be на разных строках
def task_4():
    print("\n*******************************************")
    print("Task 4")
    str_task4 = "To be or not to be"
    arr_str = str_task4.split()
    num_arr = len(arr_str) // 2
    for i in range(num_arr):
        print(f"{arr_str[i]} {arr_str[i + 1]}")


# task 5 Выведите на экран надпись «Life is what happens when you're busy making other plans» John Lennon на разных
# строках.
def task_5():
    print("\n*******************************************")
    print("Task 5")
    str_task5 = "Life is what happens when you're busy making other plans» John Lennon"
    arr_str = str_task5.split()
    print(
        f"{arr_str[0]} {arr_str[1]} {arr_str[2]} {arr_str[3]}\n{arr_str[4]}\n{arr_str[5]} {arr_str[6]} {arr_str[7]} {arr_str[8]} {arr_str[9]}\n{arr_str[10]} {arr_str[11]} ")


# task 6 Необходимо создать число, содержащее эти цифры
def task_6():
    print("\n*******************************************")
    print("Task 6")
    arr_task6 = input("Введите три числа, через запятую: ").split(",")
    arr = list(map(int, arr_task6))
    print(f'Слитно = {str(arr[0]) + str(arr[1]) + str(arr[2])}')


# task 7 Требуется найти произведение цифр написанных слитно
def task_7():
    print("\n*******************************************")
    print("Task 7")
    arr_task7 = input("Введите числа слитно: ")
    sum = 1
    for i in arr_task7:
        sum *= int(i)
    print(f"Произведение={sum}")


# task 8 Требуется вывести результат перевода метров в сантиметры, дециметры, миллиметры, мили
def task_8():
    print("\n*******************************************")
    print("Task 8")
    arr_task8 = input("Введите количество метров: ")
    # сантиметры, дециметры, миллиметры, мили
    print(f"Сантиметров = {float(arr_task8) * 100}")
    print(f"Дециметров = {float(arr_task8) * 10}")
    print(f"Миллиметров = {float(arr_task8) * 1e6}")
    print(f"Миль = {float(arr_task8) * 0.000621371}")


# task 9 Напишите программу, вычисляющую площадь треугольника
def task_9():
    print("\n*******************************************")
    print("Task 9")
    arr_task9 = input("Введите размер основания треугольника и размер высоты через пробел: ").split()
    arr = list(map(int, arr_task9))
    print(f"Площадь треугольника = {0.5 * arr[0] * arr[1]}")


# task 10 Необходимо перевернуть число и отобразить результат
def task_10():
    print("\n*******************************************")
    print("Task 10")
    arr_task10 = input("Введите число: ")
    print(f"Результат= {arr_task10[::-1]}")


if __name__ == '__main__':
    # task 1
    task_1()

    # task 2
    task_2()

    # task 3
    task_3()

    # task 4
    task_4()

    # task 5
    task_5()

    # task 6
    task_6()

    # task 7
    task_7()

    # task 8
    task_8()

    # task 9
    task_9()

    # task 10
    task_10()
