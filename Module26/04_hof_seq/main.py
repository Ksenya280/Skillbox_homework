def hofstadter_sequence(initial_values):
    first, second = initial_values
    yield first
    yield second
    sequence = [first, second]
    n = 2
    while True:
        previous1 = sequence[n - sequence[n - 1]]
        previous2 = sequence[n - sequence[n - 2]]
        current = previous1 + previous2
        n += 1
        yield current
        sequence.append(current)
        if current == second and sequence[n - 1] == first:
            break



q1 = hofstadter_sequence([1, 1])
print(next(q1))
q2 = hofstadter_sequence([1, 2])
print(next(q1))
