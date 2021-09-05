def evenSubarray(numbers, k):
    expected_arrays = []
    current_array = []
    i = 0
    j = 0
    count_odd = 0
    while i < len(numbers):
        while j < len(numbers):
            if numbers[j] % 2 == 1:
                count_odd += 1
            if count_odd > k:
                break

            current_array = current_array + [numbers[j]]

            if current_array not in expected_arrays:
                expected_arrays = expected_arrays + [current_array]
            j += 1
        i += 1
        count_odd = 0
        j = i
        current_array = []
    return len(expected_arrays)
