def binarySearch(iterable_item, target):

    start = 0
    end = len(iterable_item) - 1

    while start <= end:
        middle = (start + end) // 2
        if iterable_item[middle] == target:
            return middle
        else:
            if iterable_item[middle] < target:
                start = middle
            else:
                end = middle

numbers = [1, 2, 3, 4, 5, 6]
target = 1

print(binarySearch(numbers, target))
