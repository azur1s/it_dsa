def order_of(seat):
    return ord(seat[0]) * 1000 + int(seat[1:])

def bubble_sort(lst, last):
    current = 0
    sorted_flag = False
    total_comparisons = 0

    # loop (current <= last AND sorted is false)
    while current <= last and not sorted_flag:
        walker = last
        sorted_flag = True

        # loop (walker > current)
        while walker > current:
            total_comparisons += 1
            if order_of(lst[walker]) < order_of(lst[walker - 1]):
                sorted_flag = False

                # exchange (walker, walker-1)
                lst[walker], lst[walker - 1] = lst[walker - 1], lst[walker]
            walker -= 1

        print(lst)

        current += 1

    print(f"Comparison times: {total_comparisons}")

import json
input_list = json.loads(input())
last_idx = int(input())
bubble_sort(input_list, last_idx)