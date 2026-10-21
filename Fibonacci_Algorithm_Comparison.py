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
n_values_B = [10, 50, 100, 200, 500, 1000]
results_B = []

print("\nAlgorithm B Results")
print(f"{'n':<5} | {'calls':<15} | {'time (s)'}")
print("-" * 35)

for n in n_values_B:
    counter_B = 0
    fibtable.clear()

    start_time = time.perf_counter()

    try:
        fib_B(n)
    except RecursionError:
        print(f"{n:<5} | RECURSION LIMIT HIT")
        continue

    end_time = time.perf_counter()
    duration = end_time - start_time

    results_B.append((n, counter_B, duration))
    print(f"{n:<5} | {counter_B:<15} | {duration:.6f}")
if results_A and results_B:
    n_A, c_A, _ = zip(*results_A)
    n_B, c_B, _ = zip(*results_B)

    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.plot(n_A, c_A, marker="o", color="red")
    plt.yscale("log")
    plt.title("Algorithm A: Calls vs n (Log Scale)")
    plt.xlabel("n")
    plt.ylabel("Number of Calls")

    plt.subplot(1, 2, 2)
    plt.plot(n_B, c_B, marker="o", color="blue")
    plt.title("Algorithm B: Calls vs n")
    plt.xlabel("n")
    plt.ylabel("Number of Calls")

    plt.tight_layout()
    plt.show()
else:
    print("Unable to plot because one or both result lists are empty.")
print("\nPushing to n=1000")

print("Default recursion limit:", sys.getrecursionlimit())

fibtable.clear()
counter_B = 0

try:
    result = fib_B(1000)
    print(f"Default settings output for n=1000: {result}")
except RecursionError:
    print("Default settings: RecursionError occurred.")

sys.setrecursionlimit(2000)

fibtable.clear()
counter_B = 0

try:
    result = fib_B(1000)
    print(f"Fix 1 (Recursion Limit) Output for n=1000: {result}")
except RecursionError:
    print("Fix 1: RecursionError still occurred.")


def fib_iterative(n):
    if n == 0 or n == 1:
        return n

    table = [0] * (n + 1)
    table[1] = 1

    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]

    return table[n]


print(f"Fix 2 (Iterative) Output for n=1000: {fib_iterative(1000)}")
