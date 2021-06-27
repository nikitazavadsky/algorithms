"""It is a recursive implementation of merge sort
algorithm from 'Algorithms Illuminated Part 1 The Basics By Tim Roughgarden'"""


def merge_sort(input_array: list) -> list:
    """Returns sorted array"""

    if len(input_array) > 1:

        half_len = len(input_array)//2

        first_half = merge_sort(input_array[:half_len])
        second_half = merge_sort(input_array[half_len:])

        return merge(first_half, second_half)

    else:
        return input_array


def merge(first_half: list, second_half: list) -> list:
    """Merges two parts into the single one"""

    output_array = []
    idx_first = idx_second = 0
    for idx in range(len(first_half)+len(second_half)):

        try:
            if first_half[idx_first] < second_half[idx_second]:

                output_array.append(first_half[idx_first])
                idx_first += 1

            else:
                output_array.append(second_half[idx_second])
                idx_second += 1

        except IndexError:
            if idx_first == len(first_half):
                output_array += second_half[idx_second:]
            else:
                output_array += first_half[idx_first:]

            return output_array

    print(output_array)
    return output_array


print(merge_sort([9, 8, 7, 6, 5, 4, 3, 2]) == [2, 3, 4, 5, 6, 7, 8, 9])
