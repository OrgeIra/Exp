''' 1 misol'''
# def subtract_negative_average(list1, list2):
#     negative_numbers_list1 = [x for x in list1 if x < 0]
#     negative_numbers_list2 = [x for x in list2 if x < 0]

#     if negative_numbers_list1:
#         average_list1 = sum(negative_numbers_list1) / len(negative_numbers_list1)
#     else:
#         average_list1 = 0

#     if negative_numbers_list2:
#         average_list2 = sum(negative_numbers_list2) / len(negative_numbers_list2)
#     else:
#         average_list2 = 0

#     result = average_list1 - average_list2
#     return result

# list1 = [1, 1, 3, 4, 4, 5, 6, 7]
# list2 = [0, 1, 2, 3, 4, 4, 5, 7, 8]

# result = subtract_negative_average(list1, list2)
# print("Natija = ", result)

'''2 misol'''

# def add_string_to_elements(lst, string):
#     new_lst = [string + str(i) for i in lst]
#     return new_lst

# lst = [1, 4, 3, 9]
# string = "RM"

# result = add_string_to_elements(lst, string)
# print("Natija = :", result)

''' 3 misol '''

# def find_list_with_largest_sum(lst):
#     max_sum = float('-inf')
#     max_list = None

#     for i in lst:
#         current_sum = sum(i)
#         if current_sum > max_sum:
#             max_sum = current_sum
#             max_list = i

#     return max_list

# input_list = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]

# result = find_list_with_largest_sum(input_list)
# print("Natija = ", result)

''' 4 misol'''

# def count_integers(lst):
#     count = 0
#     for i in lst:
#         if isinstance(i, int):
#             count += 1
#     return count

# input_list = [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]

# result = count_integers(input_list)
# print("Natija = ", result)

'''5 misol'''

# def most_common_element(lst):
#     count_dict = {}

#     for i in lst:
#         if i in count_dict:
#             count_dict[i] += 1
#         else:
#             count_dict[i] = 1

#     most_common = max(count_dict, key=count_dict.get)
#     count = count_dict[most_common]

#     return most_common, count

# input_list = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]

# most_common, count = most_common_element(input_list)
# print(f"Eng kup takrorlangan {most_common} -> {count} ")


''' 6 misol '''

# def increment_list(lst):
#     num_str = ''.join(map(str, lst))
    
#     result_num = int(num_str) + 1
#     result_lst = [int(digit) for digit in str(result_num)]
    
#     return result_lst

# input_list = [1, 2, 3]
# output_list = increment_list(input_list)
# print("Natija = ", input_list, ":", output_list)

# input_list = [9]
# output_list = increment_list(input_list)
# print("Natija = ", input_list, ":", output_list)

# input_list = [9, 9, 9, 9]
# output_list = increment_list(input_list)
# print("Natija = ", input_list, ":", output_list)

''' 7 misol'''

# def squares_of_elements(n, elements):
#     elements = list(map(int, elements.split()))

#     squares = [elem ** 2 for elem in elements]
#     return squares

# n = int(input("sonnini kiriting: "))

# elements = input("cherez probel kiriting: ")

# result = squares_of_elements(n, elements)
# print("Squar: ", result)

''' 8 misol'''

# def combine_lists_with_numbers(lst1, lst2):
#     combined_list = []
#     for i in range(min(len(lst1), len(lst2))):
#         combined_item = lst2[i].lower() + str(lst1[i])
#         combined_list.append(combined_item)
#     return combined_list

# list1 = [1, 4, 3, 9]
# list2 = ['Chelci', 'Real', 'Barsa', 'my5']

# result = combine_lists_with_numbers(list1, list2)
# print("Natija: ", result)

''' 9 misol'''

# def find_largest_element_with_list(lst):
#     largest_element = None
#     max_element_in_list = float('-inf')

#     for item in lst:
#         if isinstance(item, list):
#             max_in_sublist = max(item)
#             if max_in_sublist > max_element_in_list:
#                 largest_element = max_in_sublist
#                 max_element_in_list = max_in_sublist

#     return largest_element

# input_list = [1, 2, [3, 4, 5], [6, 7], 8, [9, 10, 11, 12]]

# result = find_largest_element_with_list(input_list)
# print("Eng kattasi: ", result)

'''10 misol'''

# def fibonacci(n):
#     fib = [0, 1]
#     while fib[-1] < n:
#         fib.append(fib[-1] + fib[-2])
#     return fib[:-1]

# def nearest_fibonacci(n):
#     fib = fibonacci(n)
#     closest_fibs = [fib[-2], fib[-1]]
#     return closest_fibs

# input_number = int(input("Son kiriting: "))
# result = nearest_fibonacci(input_number)
# print("eng yaqin", input_number, "fibanachi son:", result)
