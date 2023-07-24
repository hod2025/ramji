# Selection Sort
ele = int(input("Enter the number of elements: "))
arr = []
for i in range(ele):
    value = int(input(f"Enter element {i + 1}: "))
    arr.append(value)
    
n = len(arr)
for i in range(n):
    min_idx = i
    for j in range(i + 1, n):
        if arr[j] < arr[min_idx]:
            min_idx = j

    arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Print the sorted array
print("Sorted Array:")
print(arr)
