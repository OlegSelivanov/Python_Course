# Семинар 2

"""
Задача №9. Общее обсуждение
По данному целому неотрицательному n вычислите
значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
чисел от 1 до N) 0! = 1 Решить задачу используя цикл
while
Input: 5
Output: 120
"""

# # 1
# n = int(input())
# fact = 1
# while n > 1:
#     fact *= n
#     n -= 1
 
# print(fact)

# # 2
# import math
# n = int(input('Fact: '))
# res = math.factorial(n)
# print(res)

# # 3
# n = int(input())
# if n == -1 or n == 1:
#     print(1)
# elif n > 1:
#     factorial = 1
#     for i in range(2, n + 1):
#         factorial *= i
#     print(factorial)
# elif n == 0:
#     print('1')



"""
Задача №11. Решение в группах
Дано натуральное число A > 1. Определите, каким по
счету числом Фибоначчи оно является, то есть
выведите такое число n, что φ(n)=A. Если А не
является числом Фибоначчи, выведите число -1.
Input: 5
Output: 6
"""

# # 1
# a = int(input())
# if a == 0:
#     print(0)
# else:
#     prev, next = 0, 1
#     n = 2
#     while next <= a:
#         if next == a:
#             print(n)
#             break
#         prev, next = next, prev + next
#         n += 1
#     else:
#         print(-1)

# # 2
# num = int(input())
# first = 0
# second = 1
# counter = 2
# while second <= num:
#     if second == num:
#         print(counter)
#         break
#     first, second = second, first + second
#     counter+=1
# else:
#     print(-1)

# # 3
# number = int (input ("натуральное число A > 1 - > "))

# flag = True
# i = 1
# while(flag):
#     temp = t10.fib(i)
#     if temp < number:
#         i+=1
#     elif temp == number:
#         print(i)
#         flag = False
#     else:
#         print(-1)
#         flag = False


"""
Задача №13. Решение в группах
Уставшие от необычно теплой зимы, жители решили узнать,
действительно ли это самая длинная оттепель за всю историю
наблюдений за погодой. Они обратились к синоптикам, а те, в
свою очередь, занялись исследованиями статистики за
прошлые годы. Их интересует, сколько дней длилась самая
длинная оттепель. Оттепелью они называют период, в
который среднесуточная температура ежедневно превышала
0 градусов Цельсия. Напишите программу, помогающую
синоптикам в работе.
Пользователь вводит число N – общее количество
рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
располагается N целых чисел.
Каждое число – среднесуточная температура в
соответствующий день. Температуры – целые числа и лежат в
диапазоне от –50 до 50
Input: 6 -> -20 30 -40 50 10 -10
Output: 2
"""

# n = int(input())
# s = input().split()
# t=0
# k=0
# for i in range(n):
#     if int(s[i])>0:
#         k+=1
#     else:
#         if t<k:
#             t=k
#             k=0
# if t<k:
#     t=k
# print(t)

"""
Задача №15. Решение в группах
15. Иван Васильевич пришел на рынок и решил
купить два арбуза: один для себя, а другой для тещи.
Понятно, что для себя нужно выбрать арбуз
потяжелей, а для тещи полегче. Но вот незадача:
арбузов слишком много и он не знает как же выбрать
самый легкий и самый тяжелый арбуз? Помогите ему!
Пользователь вводит одно число N – количество
арбузов. Вторая строка содержит N чисел,
записанных на новой строчке каждое. Здесь каждое
число – это масса соответствующего арбуза
Input: 5 -> 5 1 6 5 9
Output: 1 9
"""

# # 1
# n = int(input())

# if n < 2 :
#   print("Арбузов не < 2")
# else:
#   list = list(map(int,input().split()))
#   list.sort()

#   print(list[0],list[-1])

# # 2
# N = int(input(': '))
# sp = []
# for i in range(N):
#     sp.append(int(input()))
#     min = sp[0]
#     max = sp[0]
# for i in range(N):
#     if sp[i] > max:
#         max = sp[i]
#     if sp[i] < min:
#         min = sp[i]
# print(min, max)

# # 3
# N = int(input(': '))
# sp = []
# for i in range(N):
#     wm = randint(0, 10)
#     sp.append(wm)
#     min = sp[0]
#     max = sp[0]
# print(sp)
# for i in range(N):
#     if sp[i] > max:
#         max = sp[i]
#     if sp[i] < min:
#         min = sp[i]
# print(min, max)



# Семинар 3. Списки и словари

"""
Задача №17. Решение в группах
Дан список чисел. Определите, сколько в нем
встречается различных чисел.

Input: [1, 1, 2, 0, -1, 3, 4, 4]
Output: 6
"""

# print(len(set(input().split())))



"""
Задача №19. Решение в группах
Дана последовательность из N целых чисел и число
K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо, K –
положительное число.
Input: [1, 2, 3, 4, 5] k = 3
Output: [4, 5, 1, 2, 3]
"""
# # Срез
# list_2 = [1, 2, 3, 4, 5]
# k = int(input("Введите k: "))
# print(f"{list_2[len(list_2)-k:len(list_2)]} {list_2[:len(list_2)-k]}")

# # Перебор
# lst = [1, 2, 3, 4, 5]
# k = 2
# for i in range(k):
#     lst.insert(0, lst.pop(-1))
# print(lst)

"""
Задача №21. Решение в группах
Напишите программу для печати всех уникальных
значений в словаре.
Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
":" S007 "}]
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
Примечание: Список словарей задан изначально.
Пользователь его не вводит
"""

# L = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":" S005 "}, {" V ":" S009 "},{" VIII ":" S007 "}]
# print("Original List: ",L)
# u_value = set( val for dic in L for val in dic.values())
# print("Unique Values: ",u_value)


# list_dict = [{"V": "S001"}, {"V": "S002", "f": "asdfa"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
# list_uniq = []
# for d in list_dict:
#     #d = {"V": "S001", "V!": "S00f1"}
#     for val in list(d.values()):
#         # val = ["S001"; "S00f1"]
#         if val not in list_uniq:
#             list_uniq.append(val)
# print(list_uniq)


"""
Задача №23. Решение в группах
Дан массив, состоящий из целых чисел. Напишите
программу, которая подсчитает количество
элементов массива, больших предыдущего (элемента
с предыдущим номером)
Input: [0, -1, 5, 2, 3]
Output: 2 (-1 < 5, 2 < 3)
Примечание: Пользователь может вводить значения
списка или список задан изначально.
"""

# num = int(raw_input('n: '))
# inp = raw_input('list: ').split()
 
# if len(inp) != num:
#     print "ERR:", num, "vs", len(inp)
# else:
#     print len([n for n, el in enumerate(inp) if n <= len(inp)-2 and inp[n] < inp[n+1]])



# a = map(int, input().split())
# a = list(a)
# n = int(input())
# k = 0
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         k += 1
# print(k)


""" Для дом задания №20
gen_dict = eng_dict
gen_dict.update(rus_dict)

amount = 0
s = input("Введите строку: ").upper()
for c in s:
    for k, v in gen_dict.items():
        if k.find(c) >= 0:
            amount += v
            break
print(f"Стоимость слова = {amount}.")
"""



# # Семинар 4

# '''
# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз
# каждый символ уже встречался. Количество повторов добавляется к символам с помощью 
# постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a_0 a_1 a_2 b_0 c_0 a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию split()
# '''

# n = input().split()                                           
# b = {}                                                        
# for i in n:                                                  
#     if i in b:                                                
#         print(f'{i}_{b[i]}', end='  ')
#     else:
#         print(i, end=' ')
#     b[i] = b.get(i, 0) + 1




# """
# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается последовательность непробельных
# символов идущих подряд, слова разделены одним или большим числом пробелов или символами
# конца строки.
# Определите, сколько различных слов содержится в этом тексте.
# Input:
# She sells sea shells on the sea shore;The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore,I'm sure that the shells are sea
# shore shells.
# Output: 17
# """

# # 1 вариант решения через множество

# line = (input('Введите символы строки через пробел: ').lower().split())  
# multi = set()         
# for i in line:
#     multi.add(i)    
# print(len(multi))   


# # 2 вариант решения, записанное в одну строку

# print(len(set(input('Введите текст ').upper().replace('.', ' ').split())))


# # 3 вариант - решение через словарь

# n = input('Введите текст: ').split()
# dict = {}
# for i in n:
#     dict[i.lower()]=0
# print(len(dict.keys()))



"""
Задача №29. Решение в группах
Задана последовательность неотрицательных целых чисел. Требуется определить
значение наибольшего элемента последовательности, которая завершается первым
встретившимся нулем (число 0 не входит в последовательность).
"""
# if in range не подходит, т.к. мы не значем сколько чисел будет введено до 0
# в задаче вводим первую переменную в начале кода, а последующуие в цикле,
# пока не встретится 0


# n = int(input('Введите число: '))       
# max = n                                 
# while n != 0:                              
#     n = int(input('Введите число: '))   
#     if n > max:
#         max = n
# print(f'Максимальное число в введнной последовательности: {max}')


"""
Орел и решка
Дана строка текста, состоящая из букв русского алфавита "О" и "Р". Буква 
"О" – соответствует выпадению Орла, а буква "Р" – соответствует выпадению Решки. 
Напишите программу, которая подсчитывает наибольшее количество подряд выпавших Решек.
Формат входных данных
На вход программе подается строка текста, состоящая из букв русского алфавита "О" и "Р".
Формат выходных данных
Программа должна вывести наибольшее количество подряд выпавших Решек.
Примечание. Если выпавших Решек нет, то необходимо вывести число 
0
0.
"""

# s=input()
# t=0
# while "Р"*(t+1) in s:
#     t+=1
# if t!=0:
#     print(t)
# else:
#     print(0)


"""
Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников. 
Теперь он использует их в качестве серверов "Пегого дудочника". 
Помогите владельцу фирмы отыскать все зараженные холодильники.

Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр, 
и если в ней присутствует слово "anton" (необязательно рядом стоящие буквы, 
главное наличие последовательности букв), то холодильник заражен и нужно вывести номер холодильника, 
нумерация начинается с единицы

Формат входных данных
В первой строке подаётся число 
n
n – количество холодильников. В последующих 
n
n строках вводятся строки, содержащие латинские строчные буквы и цифры, в каждой строке от 
5
5 до 
100
100 символов.

Формат выходных данных
Программа должна вывести номера зараженных холодильников через пробел. 
Если таких холодильников нет, ничего выводить не нужно.

Формат входных данных
В первой строке подаётся число 
n
n – количество холодильников. В последующих 
n
n строках вводятся строки, содержащие латинские строчные буквы и цифры, в каждой строке от 
5
5 до 
100
100 символов.

Формат выходных данных
Программа должна вывести номера зараженных холодильников через пробел. 
Если таких холодильников нет, ничего выводить не нужно.

6
222anton456
a1n1t1o1n1
0000a0000n00t00000o000000n
gylfole
richard
ant0n

"""

# import re
 
# lst = []
# regex = ''.join(f'.*?{i}' for i in 'anton')
# for i in range(int(input('N: '))):
#     if re.search(regex, input()):
#         lst.append(i)
# print(lst)

# n = int(input())
# list1 = []
# for i in range(n):
#     a = input()
#     if 'a' in a:
#         a = a[a.find('a'):]
#         if 'n' in a:
#             a = a[a.find('n'):]
#             if 't' in a:
#                 a = a[a.find('t'):]
#                 if 'o' in a:
#                     a = a[a.find('o'):]
#                     if 'n' in a:
#                         list1.append(i + 1)                   
# print(*list1)


# print(*filter(lambda x:x>=0, (i if re.search('.*?'.join('anton'), input()) else -1 for i in range(int(input('N: '))))))




# # Семинар 5

""" 
Задача №31. Решение в группах
Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., 
где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи

Input: 7
Output: 21

Задание необходимо решать через рекурсию
"""

# n = int(input('Введите порядковый номер числа Фибоначчи: '))

# def fib(n):                       # создаем метод (рекурсию)
#     if n in (0, 1):               # базис рекурсии - кортеж а не список, т.к. он быстрее работает
#         return 1
#     return fib(n-1) + fib(n-2)    # сама рекурсия (формула расчета)
# print(f'Порядковому номеру {n} соответствует значение {fib(n-2)}')



"""
Задача №33. Решение в группах
Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на
максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все
максимальные – на минимальные.

Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1
"""

# import random

# # n = int(input('Введите количество оценок в журнале '))

# # jour=[]
# # for i in range(n):
# #     jour.append(random.randint(1,5))

# # сокращенная запись заменяет строки 13-17
# jour = [random.randint(1, 5) for i in range(int(input('Введите количество оценок в журнале ')))]

# print(*jour)

# max_mark = max(jour)
# min_mark = min(jour)

# for i in range(len(jour)):
#     if jour[i] == max_mark:
#         jour[i] = min_mark
# print(*jour)



"""
Задача №35. Решение в группах
Напишите функцию, которая принимает одно число и проверяет, является ли оно простым.
Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число).

Input: 5
Output: yes
"""

# def check_num(n):
#     mark = 2
#     while mark * mark <= n and n % mark != 0:
#         mark += 1
#     return mark * mark > n

# n = int(input('Введите число: '))
# if check_num(n):
#     print('YES')
# else:
#     print('NO')



"""
Задача №37. Решение в группах
Дано натуральное число N и последовательность из N элементов.
Требуется вывести эту последовательность в обратном порядке.
Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).

Input: 2 -> 3 4
Output: 4 3
"""

# # 1 Вариант
# revers = input('Введите последовательность через пробел:  ')
# print(revers[::-1])


# # 2 Вариант (Правильный)
# def revers(n):                          # Объявляем функцию
#     if n > 0:                           # Условие выхода из рекурсии. Пока n > 0 буем выполнять все что ниже в ветке if 
#         revers(n-1)                     # Рекурсивный вызов функцию revers(n-1). Когда мы в коде натыкаемся на эту строчку 
#                                         # revers(n-1) выполнение программы прерывается и в стек сохраняется исходный 
#                                         # аргумент {n}, а сам рекурсивный вызов функции происходи при (n-1) и так по кругу
#                                         # пока не достигнем нуля (n = 0). В этот момент рекурсивный вызов прерывается 
#                                         # (так как сработало условие if) и исполнение кода наконец-то переходит 
#                                         # к строке print.
#         print(sp[-n], end=" ")          # Выводим данную последовательность
# N = int(input())                        # Получаем натуральное число N
# sp = list(map(int, input().split()))    # Получаем последовательность из N элементов. Сразу создаем список
# revers(N)                               # Вызываем функцию 




# # Семинар 6

"""
Задача №39. Решение в группах
Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом
массиве), которых нет во втором массиве. Пользователь вводит число N - количество элементов в первом массиве, затем N
чисел - элементы массива. Затем число M - количество элементов во втором массиве. Затем элементы второго массива
Ввод:                   Вывод:
7                       3 3 2 12
3 1 3 4 2 4 12

6
4 15 43 1 15 1          (каждое число вводится с новой строки)
"""

# # 1 вариант

# import random
# n = int(input('Введите количество элементов первого массива: '))
# first = []
# for i in range(n):
#     first.append(random.randint(1, 101))
# m = int(input('Введите количество элементов второго массива: '))
# second = []
# for i in range(m):
#     second.append(random.randint(1, 101))
# print(first)
# print(second)
#                                     # создаем счетчик, который посчитывает
# count = 0                           # количество повторений числа во 2 массиве                    
# for i in range(n):                  # цикл проходится по первому списку
#     for j in range(m):              # и по второму, чтобы сравнить числа
#         if first[i] == second[j]:   # сравниваем число из 1 на равенстро с числами 2 списка
#             count += 1              # если есть равенство, то счетчик увеличиваем
#     if count == 0:                  # если счетчик остался равен 0, то выводим на 
#         print(first[i], end=' ')    # печать элемент 1 массива (в строку)
#     count = 0                       # если повторы были, то обнулем счетчик и 
# print('\n')                         # c новой строки, переходим к следующему элементу массива


# # 2 вариант 

# list_1 = [int(input('add element: ')) for i in range(int(input('enter n = ')))]
# list_2 = [int(input('add element: ')) for i in range(int(input('enter m = ')))]

# print([i for i in list_1 if i not in list_2])


# # 3 вариант 

# from random import randint
# num_list_1 = [randint(1, 10) for _ in range(int(input('Введите размер первого массива: ')))]
# num_list_2 = [randint(1, 10) for _ in range(int(input('Введите размер второго массива: ')))]    
# print(*num_list_1)
# print(*num_list_2)

# list1_unique_nums=set(num_list_1)-set(num_list_2)
# for i in num_list_1:
#     if i in list1_unique_nums:
#         print(i, end=' ')

# print('\n')


"""
Задача №41. Решение в группах
Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит
количество элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного.
Сначала вводится число N — количество элементов в массиве. Далее записаны N чисел — элементы
массива. Массив состоит из целых чисел.

Ввод: 
5 
1 2 3 4 5
Вывод:
0
Ввод:
5
1 5 1 5 1
Вывод:
2
"""


# import random

# n = int(input('Введите количество элементов массива: '))

# arr = []
# for i in range(n):
#     arr.append(random.randint(1, 101))

# print(arr)

# count = 0
# for i in range(n):
#     if arr[i-2] < arr[i-1] > arr[i]:   # такая нумерация не позволит выйти за пределы массива
#         count += 1

# print(count)

# # интересный вариант строки 699 с условием
# #     if arr[i-1] < arr [i] > arr [(i + 1) % len(arr)]: 
# # % когда i достигнет предела массива, деление с остатком на само себя даст 0 
# #  и превратиться в аrr[0]


# # сокращенная запись этого кода

# from random import randint

# list = [randint(1, 20) for i in range(int(input('Введите количество элементов массива: ')))]

# print(list)

# count = 0
# for i in range(len(list)):
#     if list[i-2] < list[i-1] > list[i]:   # такая нумерация не позволит выйти за пределы массива
#         count += 1

# print(count)


"""
Задача №43. Решение в группах
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
Считается, что любые два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать. 
Вводится список чисел. Все числа списка находятся на разных строках.

Ввод: 
1 2 3 2 3
Вывод:
2
"""

# from random import randint

# arr = [randint(1, 101) for i in range(int(input('Введите количество элементов массива: ')))]

# print(arr)

# count = 0
# for i in range(len(arr)-1):          # -1 чтобы последний элемент не сравнивался с последним
#     for j in range(i+1, len(arr)):   # +1 чтобы первый элемент не сравнивался с последним
#         if arr[i] == arr[j]:
#             count+=1
# print(count)


"""
Задача №45. Решение в группах
Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n
(включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа.
По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. Программа
получает на вход одно натуральное число k, не превосходящее 105. Программа должна вывести все
пары дружественных чисел, каждое из которых не превосходит k. Пары необходимо выводить по одной в
строке, разделяя пробелами. Каждая пара должна быть выведена только один раз (перестановка чисел новую
пару не дает).

Ввод:           Вывод:
300             220 284
"""


# # 1 Вариант
# def divisors(number):
#     return sum(x for x in range(1, number // 2 + 1) if number % x == 0)
    
# pairs = {}
# for i in range(int(input('Введите число: '))):
#     summ = divisors(i)
#     if summ != 1:
#         if i in pairs:
#             num1, num2 = i, pairs[i]
#             if (num1 // num2) and (divisors(num1) == num2):
#                 print(*sorted([num2, num1]))
#         else:
#             pairs[summ] = i


# # 2 Вариант
# for i in range(int(input('Введите число: '))):
#     m = 0
#     n = 0
#     for x in range(1, i):
#         if i % x == 0:
#             m += x
#     for j in range(1, m):
#         if m % j == 0:
#             n += j
#     if i == n and i != m and i == min(i, m):
#         print(i, m)




# # Семинар 7


"""
Задача №47. Решение в группах
У вас есть код, который вы не можете менять(так часто бывает, когда код в глубине
программы используется множество раз и вы не хотите ничего сломать):
transformation = <???>
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
или любой другой список transormed_values = list(map(transformation, values))
Единственный способ вашего взаимодействия с этим кодом - посредством задания
функции transformation. Однако вы поняли, что для вашей текущей задачи вам не нужно
никак преобразовывать список значений, а нужно получить его как есть.
Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
копией values.

Ввод:
values = [1, 23, 42, ‘asdfg’]
transformed_values = list(map(trasformation, values))
if values == transformed_values:
    print(‘ok’)
else:
    print(‘fail’)

Вывод:
ok
"""

# transformation = lambda x: x                # вводим в код строку, lambda (анонимную) функцию которая ничего не делает х=х
# values = [1, 23, 42, 'asdfg']                           # чтобы не писать return
# transformed_values = list(map(transformation, values))  #list функция, которая оборачивает в список работу map
#                                                         # если не поставить list, то выдаст объект map <map object at 0x000000B67783B070>                                                    
#                                                         # map применяет функцию transformation, на 
#                                                         # каждый элемент списка values
# if values == transformed_values:
#     print('ok')
# else:
#     print('fail')

# print(values)
# print(transformed_values)


"""
Задача №49. Решение в группах
Планеты вращаются вокруг звезд по эллиптическим орбитам. Назовем самой далекой планетой ту,
орбита которой имеет самую большую площадь. Напишите функцию find_farthest_orbit(list_of_orbits),
которая среди списка орбит планет найдет ту, по которой вращается самая далекая планета.
Круговые орбиты не учитывайте: вы знаете, что у вашей звезды таких планет нет, зато искусственные 
спутники были были запущены на круговые орбиты.
Результатом функции должен быть кортеж, содержащий длины полуосей эллипса орбиты самой далекой
планеты. Каждая орбита представляет из себя кортеж из пары чисел - полуосей ее эллипса.
Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b - длины полуосей эллипса.
При решении задачи используйте списочные выражения.
Подсказка: проще всего будет найти эллипс в два шага: сначала вычислить самую большую 
площадь эллипса, а затем найти и сам эллипс, имеющий такую площадь.
Гарантируется, что самая далекая планета ровно одна.

Ввод:
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))

Вывод:
2.5  10
"""

# # 1 вариант

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

# def find_farthest_orbit(orbits):
#    pi = 3.14
#    orbits_new = [(0, 0)]
#    max = 0
#    for i in orbits:
#         if i[0] != i[1]:
#             if max < pi * i[0] * i[1]:
#                max = pi * i[0] * i[1]
#                orbits_new.pop()             # если выполняется условие, то удаляем предыдущее значение кортежа
#                orbits_new.append(i)         # и добавляем новое, чтобы в списке оставалась только одно, max
#    return orbits_new[0]                     # добавили [0], чтобы распаковывался список

# print(*find_farthest_orbit(orbits))


# # 2 вариант (убрали число pi, т.к. это не влияет на нахождение max)

# def find_farthest_orbit(list_of_orbits):
#     list_of_elliptical_orbits = [i for i in list_of_orbits if i[0] != i[1]]     # возвращает число из списка, который
#                                                                                 # он принимает, где 1 элемент не равен 2
#     list_of_areas = [(i[0] * i[1]) for i in list_of_elliptical_orbits]          # возвращает произведение элементов из пред. списка
#     max_area_index = list_of_areas.index(max(list_of_areas))                    # находим max из пред.списка
#     return list_of_elliptical_orbits[max_area_index]                            # возвращает max элемент
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))



"""
Задача №51. Решение в группах
Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют
одинаковое значение некоторой характеристики, и возвращают True, если это так. Если значение
характеристики для разных объектов отличается - то False. Для пустого набора объектов, функция
должна возвращать True. Аргумент characteristic - это функция, которая принимает объект
и вычисляет его характеристику.

Ввод: 
values = [0, 2, 10, 6] 
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')

Вывод:
same
"""

# def same_by(charac, objects):                                   # charac это lambda x: x % 2, objects это values
#     list_characteristic = [charac(i) for i in objects]          # list comprehension - генератор списка
#     for i in range(len(list_characteristic) - 1):
#         if list_characteristic[i] != list_characteristic[i+1]:
#             return False
#         return True
    
# values = [0, 2, 10, 6]

# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')


# # list_characteristic = [charac(i) for i in objects]    # list comprehension - генератор списка
# # обратная запись, мы перед for ставим то, что будем заполнять через функцию и подаем параметр,
# # так как это фукнция в нашем случает это 0 % 2, 2 % 2, 10 % 2)



# Семинар 8


'''
Задача №49. Решение в группах
Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска определенной записи
   (например имя или фамилию человека)
4. Использование функций. Ваша программа не должна быть линейной
'''

# def inputText():
#     with open('tel_dir.txt', 'a', encoding='utf-8') as data:    # конструкция позволяет открывать-закрвать файл авто
#         surname = data.write(input('Введите фамилию '))
#         data.write(' ')
#         name = data.write(input('Введите имя '))
#         data.write(' ')
#         fathername = data.write(input('Введите отчество '))
#         data.write(' ')
#         phoneNumber = data.write(input('Введите номер телефона '))
#         data.write('\n')


# def printText():
#     data = open('tel_dir.txt', 'r')
#     for line in data:
#         print(line)                                              # <class 'str'>
#     data.close()

# def checkText(userInfo):
#     path = 'tel_dir.txt'
#     data = open('tel_dir.txt', 'r')

#     for line in data.readlines():
#         if userInfo in line:
#             print(line)
#     data.close()

# inputText()
# printText()
# checkText(input('Введите ИМЯ для поиска контакта: '))


# # Полный Вариант

# import time
# import string
# import secrets

# print()
# print("ТЕЛЕФОННЫЙ СПРАВОЧНИК_v1")

# # создание файла 
# filename = "Tel_book.csv" 
# myfile = open(filename, "a+") 
# myfile.close
 
# # метод главного меню 
# def main_menu(): 
#     print( "\nГЛАВНОЕ МЕНЮ\n") 
#     print( "1. Просмотреть все существующие контакты") 
#     print( "2. Добавить новый контакт") 
#     print( "3. Найти существующий контакт") 
#     print( "4. Выход") 
#     choice = input("Выберите пункт меню: ") 
#     if choice == "1": 
#         myfile = open(filename, "r+") 
#         filecontents = myfile.read() 
#         if len(filecontents) == 0: 
#             print( "Искомый контакт не обнаружен, сожалею") 
#         else: 
#             print(filecontents) 
#         myfile.close 
#         enter = input("Для продолжения нажмите Enter") 
#         main_menu() 
#     elif choice == "2": 
#         newcontact() 
#         enter = input("Для продолжения нажмите Enter") 
#         main_menu() 
#     elif choice == "3": 
#         searchcontact() 
#         enter = input("Для продолжения нажмите Enter") 
#         main_menu() 
#     elif choice == "4": 
#         print("Спасибо, что используете телефонный справочник!") 
#     else: 
#         print( "Пожалуйста, повторите ввод\n") 
#         enter = input("Для продолжения нажмите Enter")
#         main_menu()
 
# # метод поиска         
# def searchcontact(): 
#     searchname = input("Введите ИМЯ для поиска контакта: ") 
#     remname = searchname[1:] 
#     firstchar = searchname[0] 
#     searchname = firstchar.upper() + remname 
#     myfile = open(filename, "r+") 
#     filecontents = myfile.readlines() 
      
#     found = False 
#     for line in filecontents: 
#         if searchname in line: 
#             print("По вашему запросу найден контакт: ", end = " ") 
#             print( line) 
#             found = True 
#             break 
#     if found == False: 
#         print(f"Контакт {searchname} не найден в справочнике, сожалею") 
 
# # имя 
# def input_firstname(): 
#     first = input("Введите ваше имя: ") 
#     remfname = first[1:] 
#     firstchar = first[0] 
#     return firstchar.upper() + remfname 
 
# # фамилия 
# def input_lastname(): 
#     last = input("Введите вашу фамилию: ") 
#     remlname = last[1:] 
#     firstchar = last[0] 
#     return firstchar.upper() + remlname

# # метод генерации ключа
# def key_gen():
#     alphabet = string.ascii_letters + string.digits
#     key = ''.join(secrets.choice(alphabet) for i in range(4))
#     return key
# key = key_gen()
 
# # сохранение новых данных контакта 
# def newcontact(): 
#     firstname = input_firstname() 
#     lastname = input_lastname() 
#     phoneNum = input("Введите ваш номер телефона: ") 
#     emailID = input("Введите ваш E-mail: ") 
#     contactDetails =(f"{key};" + firstname + " " + lastname + ";" + phoneNum + ";" + emailID +  "\n") 
#     myfile = open(filename, "a") 
#     myfile.write(contactDetails) 
#     print("Новая запись в телефонном справочнике: \n " + contactDetails + " успешно создана!")  
 
# main_menu()
# time.sleep(5)



# # Написать программу, которая выводит из списка двузначные числа

# # Вариант 1

# numbers = [8, 11, 0, -23, 140, 65, 1996]
# number_new = list(filter(lambda x: 9 < x < 100 or -9 > x > -100, numbers))
# print(number_new)


# # Вариант 2

# print(*filter(lambda x: len(str(abs(int(x)))) == 2, input().split()))


# # Преобразовать набор списков

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]

# a,b,c = map(list, zip(users, ids, salary))
# print(a, b, c, sep= "\n")
# a,b,c = map(list, zip(a, b, c))
# print(a, b, c, sep= "\n")


"""
Вводится натуральное число N. С помощью list conprehension сформировать двумерный список NxN,
состоящий из нулей, а по главной диоганали еденицы. (Главная диагональ - это элементы идущие по диагонали
от левого верхнего угла матрицы до ее нижнего правого угла). Результат вывести ввиде таблицы чисел 
как показанно в примере ниже.

Sample Input:
4
Sample Output:
1 0 0 0
0 1 0 0
0 0 1 0
0 0 0 1
"""

# # Вариант 1

# def get_matrix(n):
#     return [[int(i == j) for i in range(n)] for j in range(n)]

# if __name__ == "__main__":
#     print(*get_matrix(4), sep= "\n")


# # Вариант 2

# n = int(input('Введите размер матрицы: '))
# lst = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
# for r in lst:
#     print(*r)


'''
Вводится строка. Требуется используя введенную строку, сформировать N=10 пар кортежей в формате:

(Символ, порядковый индекс)

Первый индекс имеет значение = 0. Строка может быть короче 10 символов, а может быть и длинее.
То есть, число пар может быть 10 и менее. Используя функцию zip сформируйте указанные кортежи и
сохраните в список с иенем lst.
'''

# def _res(text):
#     return (list(zip(text, range(0, 11))))

# if __name__ == "__main__":
#     lst = _res('прикол звон')
#     print(lst)

