import time


def my_timer(function):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        function(*args, **kwargs)
        end_time = time.time()
        print(f"Execution engine: {end_time-start_time}")

    return wrapper


@my_timer
def compute(x):
    y = 1
    for i in range(1, x):
        y = y * i
    print(y)


compute(10)
