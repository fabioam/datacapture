import matplotlib.pyplot as plt
from timeit import repeat


ARRAY_LENGTH_INITIAL = 1000

if __name__ == "__main__":
    registers = []
    times = []

    print(f"array size | execution time (seconds) | execution time for each element (seconds)")
    for _ in range(40):
        setup_code = f"from random import randint;from main import DataCapture; " \
                     f"capture = DataCapture(); " \
                     f"capture.input_data = []; " \
                     f"[capture.add(i) for i in [randint(1, 1000) for i in range({ARRAY_LENGTH_INITIAL})]]"
        stmt = f"capture.build_stats()"

        last_time_execution = repeat(setup=setup_code, stmt=stmt, repeat=3, number=5)
        times.append(min(last_time_execution))
        timeindividual = min(last_time_execution)/ARRAY_LENGTH_INITIAL
        print(f" {ARRAY_LENGTH_INITIAL} | {min(last_time_execution)} | {timeindividual}  ")

        registers.append(ARRAY_LENGTH_INITIAL)

        ARRAY_LENGTH_INITIAL = ARRAY_LENGTH_INITIAL + 1000

    plt.plot(registers, times, 'b')

    plt.xlabel('registers')
    plt.ylabel('time (in seconds)')
    plt.title('Time Complexity of method build_stats()')

    plt.show()
