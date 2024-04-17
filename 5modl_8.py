# 1 misol
# from itertools import product

# def time_to_seconds(time):
#     hours, minutes, seconds = map(int, time.split(':'))
#     return hours * 3600 + minutes * 60 + seconds

# def seconds_to_time(seconds):
#     hours = seconds // 3600
#     seconds %= 3600
#     minutes = seconds // 60
#     seconds %= 60
#     return '{:02}:{:02}:{:02}'.format(hours, minutes, seconds)

# def time_difference(time1, time2):
#     seconds1 = time_to_seconds(time1)
#     seconds2 = time_to_seconds(time2)
#     return abs(seconds2 - seconds1)

# time1 = input("Введите первое время в формате HH:MM:SS: ")
# time2 = input("Введите второе время в формате HH:MM:SS: ")

# difference = time_difference(time1, time2)
# print("Разница между указанными временами составляет {} секунд.".format(difference))

# 2 misol

# import itertools

# def even_divisors(n):
#     return (i for i in itertools.count(2, 2) if n % i == 0)

# n = 24
# even_divisors_list = list(even_divisors(n))
# count_even_divisors = len(even_divisors_list)

# print("Четные делители числа", n, ":", even_divisors_list)
# print("Количество четных делителей числа", n, ":", count_even_divisors)

# 3 misol

# def odd_numbers_generator(n):
#     for num in range(1, n+1, 2):
#         yield num

# n = int(input("Введите число: "))
# print("Нечетные числа до {}: ".format(n))
# for odd_num in odd_numbers_generator(n):
#     print(odd_num, end=" ")

# 4 misol

# from itertools import count, takewhile

# def prime_factors_generator(n):
#     divisor = 2
#     while n > 1:
#         if n % divisor == 0:
#             yield divisor
#             n //= divisor
#         else:
#             divisor += 1

# number = int(input("Введите число: "))
# print("Простые делители числа {}: ".format(number), end="")
# prime_factors = prime_factors_generator(number)
# primes_up_to_n = takewhile(lambda x: x <= number, prime_factors)
# print(*primes_up_to_n, end=" ")

# 5 misol

# from itertools import chain

# def even_numbers_generator(numbers):
#     for num in numbers:
#         if isinstance(num, int):
#             if num % 2 == 0:
#                 yield num
#         elif isinstance(num, list):
#             yield from even_numbers_generator(num)

# # Пример использования генератора
# input_list = [1, 2, [3, 4, [5, 6], 7], 8, [9, [10, 11]], 12]
# even_nums = even_numbers_generator(input_list)
# print("Четные числа в последовательности чисел:")
# print(*even_nums)

# 6 misol

# from itertools import chain

# def word_length_generator(text):
#     words = text.split()
#     return (len(word) for word in words)

# text = "Это пример текста для проверки функции."
# lengths = word_length_generator(text)
# print("Длины слов в тексте:")

# print(*lengths)

# 7 misol

# from itertools import filterfalse

# def words_over_five_chars(text):
#     return filterfalse(lambda word: len(word) <= 5, text.split())

# text = "Это пример текста для проверки функции генератора."
# long_words = words_over_five_chars(text)
# print("Слова длинее 5 символов в тексте:")
# print(*long_words)

# 8 misol

# from itertools import groupby

# def numbers_with_three_or_more_occurrences(sequence):
#     sorted_sequence = sorted(sequence)
#     return (key for key, group in groupby(sorted_sequence) if len(list(group)) >= 3)

# sequence = [1, 2, 3, 3, 4, 5, 3, 2, 2, 3, 1, 3, 3]
# numbers = numbers_with_three_or_more_occurrences(sequence)
# print("Числа, встречающиеся три или более раз:")
# print(*numbers)
