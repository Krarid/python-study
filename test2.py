def average_by_key(pairs: list[tuple]) -> dict:
    sums: dict = {}
    counts: dict = {}

    for key, value in pairs:
        sums[key] = sums.get(key, 0) + value
        counts[key] = counts.get(key, 0) + 1

    return {k: sums[k] / counts[k] for k in sums}

list_tuples: list[tuple] = [('A', 1), ('B', 2), ('C', 3), ('A', 5), ('A', 9), ('A', 10), ('C', 6)]

print(average_by_key(list_tuples))

# Another comment
# Comment
# Another comment
# Test
# Another comment
# TESSSSST


print("Me mama la cerveza artesanal")