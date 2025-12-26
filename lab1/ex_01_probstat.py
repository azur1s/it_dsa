print(
    sum(
        sorted(
            [int(input()) for _ in range(4)],
            reverse=True
        )[:3]))