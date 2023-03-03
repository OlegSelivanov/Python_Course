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




# Семинар 5

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

# def fib(n):           # создаем метод (рекурсию)
#     if n in (0, 1):    # базис рекурсии - кортеж а не список, т.к. он быстрее работает
#         return 1
#     return fib(n-1) + fib(n-2) # сама рекурсия (формула расчета)
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

# revers = input('Введите последовательность через пробел:  ')
# print(revers[::-1])