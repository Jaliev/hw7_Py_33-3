import random
# 1) Сортировка пузырьком (Buble sort)
random_numbers = [random.randint(1, 100) for i in range(10)]
print('Рандомные числа №1:'.upper(), random_numbers)

numbers = len(random_numbers)
for i in range(0, numbers-1):
    for j in range(0, numbers-1-i):
        if random_numbers[j] > random_numbers[j+1]:
            random_numbers[j], random_numbers[j+1] = random_numbers[j+1], random_numbers[j]
print('Сортировка пузырьком:', random_numbers)

# 2) Сортировка выбором (Selection sort)
random_numbers2 = [random.randint(1, 100) for i in range(10)]
print('Рандомные числа №2:'.upper(), random_numbers2)

def selection_sort(random_numbers2):
    for i in range(len(random_numbers2)):
        min_value = i
        for j in range(i, len(random_numbers2)):
            if random_numbers2[min_value] > random_numbers2[j]:
                min_value = j
        random_numbers2[i], random_numbers2[min_value] = random_numbers2[min_value], random_numbers2[i]
    return random_numbers2
print('Сортировка выбором:', selection_sort(random_numbers2))

# 3) Сортировка вставками (Insertion sort)
random_numbers3 = [random.randint(1, 100) for i in range(10)]
print('Рандомные числа №3:'.upper(), random_numbers3)

def insertion_sort(random_numbers3):
    for i in range(1, len(random_numbers3)):
        value = random_numbers3[i]
        j = i - 1
        while j >= 0:
            if value < random_numbers3[j]:
                random_numbers3[j+1] = random_numbers3[j]
                random_numbers3[j] = value
                j = j - 1
            else:
                break
insertion_sort(random_numbers3)
print('Сортировка вставками:', random_numbers3)

# 4) Сортировка слиянием (Merge sort)
random_numbers4 = [random.randint(1, 100) for i in range(10)]
print('Рандомные числа №4:'.upper(), random_numbers4)

def merge_2_list(a, b):
    numbers = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            numbers.append(a[i])
            i += 1
        else:
            numbers.append(b[j])
            j += 1
    numbers += a[i:] + b[j:]
    return numbers
def merge_sort(random_numbers4):
    if len(random_numbers4) == 1:
        return random_numbers4
    middle = len(random_numbers4)//2
    left = merge_sort(random_numbers4[:middle])
    right = merge_sort(random_numbers4[middle:])
    return merge_2_list(left, right)
print('Сортировка слиянием:', merge_sort(random_numbers4))