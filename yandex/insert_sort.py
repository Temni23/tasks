def insertion_sort(array):
    for j in range(1, (len(array))):
        item_to_insert = array[j]
        while j > 0 and item_to_insert < array[j - 1]:
            array[j] = array[j - 1]
            j -= 1
        array[j] = item_to_insert
        print(f'step {j}, sorted {j + 1} elements: {array}')


insertion_sort([145, 88, 14, 16, 2, 23, 17, 7, 77])
