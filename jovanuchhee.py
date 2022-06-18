# numbers = [3, 5, 1, 7, 3, 9]
#
# num = [n * 2 for n in numbers]
#
# print(num)

import time


# defining function to execute for loop
def for_loop(num):
    l = []
    for i in range(num):
        l.append(i + 10)
    return l


# defining function to execute list comprehension
def list_comprehension(num):
    return [i + 10 for i in range(num)]


# Giving values to the functions

# Calculating time taken by for loop
start = time.time()
for_loop(10000000)
end = time.time()

print('Time taken by for loop:', (end - start))

# Calculating time taken by list comprehension
start = time.time()
list_comprehension(10000000)
end = time.time()

print('Time taken by list comprehension:', (end - start))

