# task 4
# Напишите функцию, которая отображает на экран форматированный текст, указанный ниже:
def task_4():
    str_task = """“Don't compare yourself with anyone in this world…
if you do so, you are insulting yourself.“
Bill Gates
"""
    print(str_task)


# task 5
# Напишите функцию, которая принимает два числа
# в качестве параметра и отображает все четные числа
# между ними.

def task_5():
    print("*******************************************")
    print("Task 5")
    arr_task = input("Введите два числа: начало и конец интервала ").split()
    arr = list(map(int, arr_task))
    if arr[1] >= arr[0]:
        left = arr[0]
        right = arr[1]
    else:
        left = arr[1]
        right = arr[0]
    for i in range(left, right + 1):
        if i % 2 == 0:
            print(i)


# task 7
# Найти минимальное из пяти чисел
def task_7(num_arr):
    min_num = num_arr[0]
    for i in range(1, len(num_arr)):
        if num_arr[i] < min_num:
            min_num = num_arr[i]
    print(f"Minimal number = {min_num}")


# task 8
# Напишите функцию, которая возвращает произведение чисел в указанном диапазоне.
def task_8():
    print("*******************************************")
    print("Task 8")
    arr_task = input("Введите два числа: начало и конец интервала ").split()
    arr = list(map(int, arr_task))
    if arr[1] >= arr[0]:
        left = arr[0]
        right = arr[1]
    else:
        left = arr[1]
        right = arr[0]
    product_num = 1
    for i in range(left, right + 1):
        product_num *= i
    print(f"Произведение чисел = {product_num}")


# task 9
# Напишите функцию, которая считает количество цифр в числе
def task_9():
    print("*******************************************")
    print("Task 9")
    arr_task = input("Введите число ")
    print(f"Количество цифр = {len(arr_task)}")


# task 10
# Напишите функцию, которая считает количество цифр в числе
def task_10():
    print("*******************************************")
    print("Task 10")
    arr_task = input("Введите число на проверку на палиндрома ")
    if len(arr_task) % 2 == 1:
        print(False)
        return False
    s1 = arr_task[:len(arr_task) // 2]
    s2 = arr_task[len(arr_task) // 2:]
    if s1 == s2:
        print(True)
        return True
    else:
        print(False)
        return False


if __name__ == '__main__':
    task_4()

    task_5()

    print("*******************************************")
    print("Task 7")
    arr_task = input("Введите пять чисел через пробел ").split()
    arr = list(map(int, arr_task))
    task_7(arr)

    task_8()

    task_9()

    task_10()
