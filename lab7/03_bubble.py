import ast

def bubbleSort(lst, last):
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
            if lst[walker] < lst[walker - 1]:
                sorted_flag = False

                # exchange (walker, walker-1)
                lst[walker], lst[walker - 1] = lst[walker - 1], lst[walker]
            walker -= 1

        print(lst)

        current += 1

    print(f"Comparison times: {total_comparisons}")

if __name__ == "__main__":
    input_list = ast.literal_eval(input().strip())
    last_idx = int(input().strip())
    bubbleSort(input_list, last_idx)