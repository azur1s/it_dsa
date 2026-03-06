import json

cities = json.loads(input())
n = int(input())
radios = [json.loads(input()) for _ in range(n)]

uncovered = set(cities)
chosen = []

while uncovered:
    # If there are no more radios to choose from, break the loop
    if not radios:
        break

    # Find the radio that covers the largest number of uncovered cities
    best_set = max(
        radios,
        key=lambda s: len(set(s["Cities"]) & uncovered)
    )

    # If the best radio cover 0 uncovered cities, break the loop (no more progress can be made)
    if len(set(best_set["Cities"]) & uncovered) == 0:
        break

    chosen.append(best_set["Name"])
    uncovered -= set(best_set["Cities"])
    radios.remove(best_set)

print(sorted(chosen))
