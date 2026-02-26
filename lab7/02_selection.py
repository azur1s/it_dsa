def selection_sort(lst, last):
    current = 0
    total_comparisons = 0

    # loop (until last element sorted)
    while current < last:
        smallest = current
        walker = current + 1

        # loop (walker <= last)
        while walker <= last:
            total_comparisons += 1
            if lst[walker] < lst[smallest]:
                smallest = walker
            walker += 1

        # exchange (current, smallest)
        lst[current], lst[smallest] = lst[smallest], lst[current]

        print(lst)

        current += 1

    print(f"Comparison times: {total_comparisons}")

import json
input_list = json.loads(input())
last_idx = int(input())
selection_sort(input_list, last_idx)