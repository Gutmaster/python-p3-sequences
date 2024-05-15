#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci = []
    for i in range(length):
        if i < 2:
            fibonacci.append(i)
        else:
            fibonacci.append(fibonacci[-1] + fibonacci[-2])
    print(fibonacci)