import random
import time


def get_me_random_list(n):
    """Generate list of n elements in random order"""
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list


def insertion_sort(a_list):
    start = time.time()

    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1

        a_list[position] = current_value

    time_spent = time.time() - start
    return a_list, time_spent


def shell_sort(a_list):
    start = time.time()

    sublistcount = len(a_list) // 2

    while sublistcount > 0:
        for startposition in range(sublistcount):
            gap_insertion_sort(a_list, startposition, sublistcount)

        sublistcount = sublistcount // 2

    time_spent = time.time() - start
    return a_list, time_spent


def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i

        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap

        a_list[position] = current_value


def python_sort(a_list):
    start = time.time()

    a_list.sort()

    time_spent = time.time() - start
    return a_list, time_spent


def main():
    list_sizes = [500, 1000, 5000]

    for the_size in list_sizes:
        insertion_total = 0
        shell_total = 0
        python_total = 0

        for i in range(100):
            my_list = get_me_random_list(the_size)
            sorted_list, time_spent = insertion_sort(my_list)
            insertion_total += time_spent

        for i in range(100):
            my_list = get_me_random_list(the_size)
            sorted_list, time_spent = shell_sort(my_list)
            shell_total += time_spent

        for i in range(100):
            my_list = get_me_random_list(the_size)
            sorted_list, time_spent = python_sort(my_list)
            python_total += time_spent

        insertion_avg = insertion_total / 100
        shell_avg = shell_total / 100
        python_avg = python_total / 100

        print(f"\nList size: {the_size}")

        print(
            f"Insertion Sort took {insertion_avg:10.7f} "
            f"seconds to run, on average"
        )

        print(
            f"Shell Sort took {shell_avg:10.7f} "
            f"seconds to run, on average"
        )

        print(
            f"Python Sort took {python_avg:10.7f} "
            f"seconds to run, on average"
        )


if __name__ == "__main__":
    main()

