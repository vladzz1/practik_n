from datetime import datetime 

# завдання 1

def get_even_numbers(start, end):
    i = start
    while i <= end:
        if i % 2 == 0:
            yield i
        i += 1

for item in get_even_numbers(5, 23):
    print(item, end=" ")

# завдання 2

def get_numbers_out_of_range(arr, start, end):
    for item in arr:
        if item < start or item > end:
            yield item

print()
for item in get_numbers_out_of_range([2, 6, 7, 12, 14, 17, 21, 24, 27, 34, 42, 54, 64], 14, 32):
    print(item, end=" ")

# завдання 3

def show_line(symbol, function_to_call):
    function_to_call(symbol)

def horizontal_line(symbol):
    i = 0
    while i < 10:
        print(symbol, end="")
        i += 1

def vertical_line(symbol):
    i = 0
    while i < 10:
        print(symbol)
        i += 1

print()
show_line("/", horizontal_line)
print()
show_line("*", vertical_line)

# завдання 4

def decorator(func):
    def private_decorator(*args, **kwargs):
        start_time = datetime.now().time()
        func(*args, **kwargs)
        dummy_date = datetime.now()
        end_time = datetime.now().time()
        dt1 = datetime.combine(dummy_date, start_time)
        dt2 = datetime.combine(dummy_date, end_time)
        print("використано часу: ", dt2 - dt1)
    return private_decorator

@decorator
def use_decorator(start, end):
    i = start
    arr = []
    while i <= end:
        if i % 2 == 0:
            arr.append(i)
        i += 1
    print(arr)

use_decorator(34, 5640)