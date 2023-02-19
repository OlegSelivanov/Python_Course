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

