import time
import random


def get_me_random_list(n):
    """Generate list of n elements in random order"""
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list


def sequential_search(a_list, item):
    start = time.time()

    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1

    time_spent = time.time() - start
    return found, time_spent


def ordered_sequential_search(a_list, item):
    start = time.time()

    pos = 0
    found = False
    stop = False

    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos + 1

    time_spent = time.time() - start
    return found, time_spent


def binary_search_iterative(a_list, item):
    start = time.time()

    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2

        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    time_spent = time.time() - start
    return found, time_spent


def binary_search_recursive(a_list, item):
    start = time.time()

    def recursive_search(a_list, item):
        if len(a_list) == 0:
            return False
        else:
            midpoint = len(a_list) // 2

            if a_list[midpoint] == item:
                return True
            else:
                if item < a_list[midpoint]:
                    return recursive_search(a_list[:midpoint], item)
                else:
                    return recursive_search(a_list[midpoint + 1:], item)

    found = recursive_search(a_list, item)
    time_spent = time.time() - start

    return found, time_spent


def main():
    sizes = [500, 1000, 5000]
    search_item = 99999999

    for the_size in sizes:
        sequential_total = 0
        ordered_total = 0
        iterative_total = 0
        recursive_total = 0

        for i in range(100):
            mylist = get_me_random_list(the_size)

            # Sequential search does not require a sorted list
            check, time_spent = sequential_search(mylist, search_item)
            sequential_total += time_spent

            # The other search methods require a sorted list.
            # Sorting is done before timing the searches.
            sorted_list = sorted(mylist)

            check, time_spent = ordered_sequential_search(
                sorted_list, search_item
            )
            ordered_total += time_spent

            check, time_spent = binary_search_iterative(
                sorted_list, search_item
            )
            iterative_total += time_spent

            check, time_spent = binary_search_recursive(
                sorted_list, search_item
            )
            recursive_total += time_spent

        sequential_avg = sequential_total / 100
        ordered_avg = ordered_total / 100
        iterative_avg = iterative_total / 100
        recursive_avg = recursive_total / 100

        print(f"\nList size: {the_size}")

        print(
            f"Sequential Search took {sequential_avg:10.7f} "
            f"seconds to run, on average"
        )

        print(
            f"Ordered Sequential Search took {ordered_avg:10.7f} "
            f"seconds to run, on average"
        )

        print(
            f"Binary Search Iterative took {iterative_avg:10.7f} "
            f"seconds to run, on average"
        )

        print(
            f"Binary Search Recursive took {recursive_avg:10.7f} "
            f"seconds to run, on average"
        )


if __name__ == "__main__":
    main() 