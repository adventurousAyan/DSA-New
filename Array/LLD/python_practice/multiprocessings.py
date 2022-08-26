import multiprocessing as mp
import time


def calc_power_one(x):
    res = []
    for num in range(1, x):
        res.append(num ** 3)


def calc_power_two(x):
    res = []
    for num in range(1, x):
        res.append(num ** 4)


def calc_power_three(x):
    res = []
    for num in range(1, x):
        res.append(num ** 2)


if __name__ == "__main__":
    start_time = time.time()
    calc_power_one(1000000)
    calc_power_two(1000000)
    calc_power_three(1000000)
    end_time = time.time()

    print(f"Time taken:{end_time - start_time}")

    print("***** Now with multiprocessing******")

    p1 = mp.Process(target=calc_power_one, args=(1000000,))
    p2 = mp.Process(target=calc_power_two, args=(1000000,))
    p3 = mp.Process(target=calc_power_three, args=(1000000,))
    start_time = time.time()
    p1.start()
    p2.start()
    p3.start()
    end_time = time.time()
    print(f"Time taken:{end_time - start_time}")
