# Take input from the user and split it into a list of integers
input_list = [int(x) for x in input("Enter space-separated integers to be sorted: ").split()]

# Perform insertion sort
n = len(input_list)
for i in range(1, n):
    key = input_list[i]
    j = i - 1
    while j >= 0 and key < input_list[j]:
        input_list[j + 1] = input_list[j]
        j -= 1
    input_list[j + 1] = key

# Display the sorted list
print("Sorted list:", input_list)
