def binary_search(arr, number):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (low + high) // 2
        
        if(arr[mid] < number):
            low = mid + 1

        elif(arr[mid] > number):
            high = mid - 1

        else:
            return mid;

        return -1


with open("inputs.in") as file:
    content = file.read().splitlines()

for x in range(len(content) - 1):
    content[x] = int(content[x])

numberToFind = int(input("Enter a number"))

result = binary_search(content, numberToFind)

print("Number found at index, ", result)