import time
import sys
import matplotlib.pyplot as plt

counter_A = 0
counter_B = 0
fibtable = {}


def fib_A(n):
    global counter_A
    counter_A += 1

    if n == 0 or n == 1:
        return n

    return fib_A(n - 1) + fib_A(n - 2)


def fib_B(n):
    global counter_B
    counter_B += 1

    if n in fibtable:
        return fibtable[n]

    if n == 0 or n == 1:
        value = n
    else:
        value = fib_B(n - 1) + fib_B(n - 2)

    fibtable[n] = value
    return value


print("Verifying outputs for n=0 to 20")

for i in range(21):
    assert fib_A(i) == fib_B(i), f"Mismatch at n={i}"

print("Verification passed.\n")
n_values_A = [5, 10, 15, 20, 25, 30, 35]
results_A = []

print("Algorithm A Results")
print(f"{'n':<5} | {'calls':<15} | {'time (s)'}")
print("-" * 35)

for n in n_values_A:
    counter_A = 0

    start_time = time.perf_counter()
    fib_A(n)
    end_time = time.perf_counter()

    duration = end_time - start_time

    results_A.append((n, counter_A, duration))
    print(f"{n:<5} | {counter_A:<15} | {duration:.6f}")

    if duration > 60:
        print(f"Algorithm A exceeded 60 seconds at n={n}.")
        break
