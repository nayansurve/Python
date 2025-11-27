# Program 2: Find largest number
arr = [12, 45, 7, 89, 23]

largest = arr[0]

for num in arr:
    if num > largest:
        largest = num

print("Largest number is:", largest)
