"""Create a list of lists of integers representing
the Pascal's triangle of `n`
"""


def pascal_triangle(n):
    """Returns pascal triangle as a list of lists
    of integers
    """
    if n <= 0:
        return []

    array = [[1]]

    for i in range(n - 1):
        new_array = []
        copy_array = array[i].copy()
        copy_array.insert(0, 0)
        copy_array.append(0)
        for j in range(len(copy_array) - 1):
            sum_arr = copy_array[j] + copy_array[j+1]
            new_array.append(sum_arr)
        array.append(new_array)
    return array
