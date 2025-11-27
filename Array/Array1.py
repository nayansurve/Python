# Program 4: Search element in array
arr = [5, 8, 12, 20, 50]

element = int(input("Enter number to search: "))

if element in arr:
    print(element, "found in array!")
else:
    print(element, "not found!")
