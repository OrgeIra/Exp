# 1 misol
# import threading
# import time

# def add(a, b):
#     print("Adding numbers...")
#     time.sleep(2) 
#     return a + b

# def subtract(a, b):
#     print("Subtracting numbers...")
#     time.sleep(3)  
#     return a - b

# def multiply(a, b):
#     print("Multiplying numbers...")
#     time.sleep(1) 
#     return a * b

# def divide(a, b):
#     print("Dividing numbers...")
#     time.sleep(2)  
#     if b == 0:
#         return "Error: Division by zero"
#     return a / b

# def main():
#     start_time = time.time()
    
#     threads = []
#     results = []

#     a = 10
#     b = 5

#     for func in [add, subtract, multiply, divide]:
#         thread = threading.Thread(target=lambda: results.append(func(a, b)))
#         threads.append(thread)
#         thread.start()

#     for thread in threads:
#         thread.join()

#     for result in results:
#         print("Result:", result)

#     end_time = time.time()
#     print("Total execution time:", end_time - start_time, "seconds")

# if __name__ == "__main__":
#     main()
# 2 misol

# import multiprocessing

# def find_pairs(numbers, target_sum, result_queue):
#     pairs = []
#     for i in range(len(numbers)):
#         for j in range(i + 1, len(numbers)):
#             if numbers[i] + numbers[j] == target_sum:
#                 pairs.append((numbers[i], numbers[j]))
#     result_queue.put(pairs)

# def main():
#     numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11]
#     target_sum = 120

#     result_queue = multiprocessing.Queue()

#     processes = []
#     for i in range(4):
#         start_index = i * len(numbers) // 4
#         end_index = (i + 1) * len(numbers) // 4
#         process = multiprocessing.Process(target=find_pairs, args=(numbers[start_index:end_index], target_sum, result_queue))
#         processes.append(process)
#         process.start()

#     for process in processes:
#         process.join()

#     all_pairs = []
#     while not result_queue.empty():
#         all_pairs.extend(result_queue.get())

#     print("Pairs with sum", target_sum, ":")
#     for pair in all_pairs:
#         print(pair)

# if __name__ == "__main__":
#     main()

# 4 misol

# import threading

# def check_agreement(name, length):

#   if length > 5:
   
#     return True  
#   else:
#     return False  

# def run_task(names):
  
#   for name in names:
#     length = len(name) 
#     result = check_agreement(name, length)
#     print(f"Имя '{name}' ({length} букв): {result}")

# if __name__ == "__main__":
#   names1 = ["Иван", "Мария", "Петр", "София", "Анастасия", "Михаил"]
#   names2 = ["Дмитрий", "Ольга", "Александр", "Елена", "Владимир", "Наталья"]
#   names3 = ["Андрей", "Ирина", "Сергей", "Татьяна", "Евгений", "Юлия"]

#   thread1 = threading.Thread(target=run_task, args=(names1,))
#   thread2 = threading.Thread(target=run_task, args=(names2,))
#   thread3 = threading.Thread(target=run_task, args=(names3,))

#   thread1.start()
#   thread2.start()
#   thread3.start()

#   thread1.join()
#   thread2.join()
#   thread3.join()

#  5 misol
# import math
# from concurrent.futures import ThreadPoolExecutor

# def is_prime(n):
#     if n <= 1:
#         return False
#     if n <= 3:
#         return True
#     if n % 2 == 0 or n % 3 == 0:
#         return False
#     i = 5
#     while i * i <= n:
#         if n % i == 0 or n % (i + 2) == 0:
#             return False
#         i += 6
#     return True

# def is_prime_or_complex(numbers):
#     results = {}
#     with ThreadPoolExecutor(max_workers=4) as executor:
#         futures = {executor.submit(is_prime, number): number for number in numbers}
#         for future in futures:
#             number = futures[future]
#             try:
#                 results[number] = future.result()
#             except Exception as exc:
#                 results[number] = False  
#     return results

# numbers = [11, 15, 23, 100, 101]
# results = is_prime_or_complex(numbers)
# for number, is_prime in results.items():
#     print(f"{number} простое: {is_prime}")

# 6 misol

# def sort_negative_integers(input_file, output_file):
#     try:
#         with open(input_file, 'r') as file:
#             numbers = [int(line.strip()) for line in file if int(line.strip()) < 0]
#             sorted_numbers = sorted(numbers, reverse=True)
#             with open(output_file, 'w') as out_file:
#                 for number in sorted_numbers:
#                     out_file.write(str(number) + '\n')
#     except FileNotFoundError:
#         print(f"Файл '{input_file}' не найден.")
#     except ValueError:
#         print("В файле содержатся некорректные данные, ожидались только отрицательные целые числа.")

# # Пример использования
# sort_negative_integers('input.txt', 'output.txt')

# 7 misol

# def remove_adjacent_duplicates(s):
#     stack = []
#     for char in s:
#         if stack and stack[-1] == char:
#             stack.pop()
#         else:
#             stack.append(char)
#     return ''.join(stack) if stack else "Empty String"

# # Пример использования
# inputs = [
#     "aaabccddd",
#     "AA",
#     "Baab"
# ]

# for idx, s in enumerate(inputs, start=1):
#     print(f"input {idx}: {s}")
#     print(f"output {idx}: {remove_adjacent_duplicates(s)}")


