def insertion_sort(lst, last):
    current = 1
    total_comparisons = 0

    # loop (until last element sorted)
    while current <= last:
        # move current element to hold
        hold = lst[current]

        walker = current - 1

        # loop (walker >= 0 AND hold key < walker key)
        while walker >= 0:
            total_comparisons += 1
            if hold < lst[walker]:
                lst[walker + 1] = lst[walker]
                walker -= 1
            else:
                break

        lst[walker + 1] = hold

        print(lst)

        current += 1

    print(f"Comparison times: {total_comparisons}")

import json
input_list = json.loads(input())
last_idx = int(input())

insertion_sort(input_list, last_idx)