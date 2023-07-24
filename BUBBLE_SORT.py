# Perform bubble sort Algortihm
input_list = [int(x) for x in input("Enter space-separated integers to be sorted: ").split()]
n = len(input_list)
for i in range(n):
    swapped = False
    for j in range(0, n - i - 1):
        if input_list[j] > input_list[j + 1]:
            input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
            swapped = True
    if not swapped:
        break
print("Sorted list:", input_list)