#!/usr/bin/env python3

def happy_new_year():
    x = 10
    while x > 0:
        print(x)
        x -= 1
    print("Happy New Year!")


def square_integers(nums):
    return [num ** 2 for num in nums]


def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

