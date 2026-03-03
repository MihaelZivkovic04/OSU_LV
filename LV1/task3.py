
numbers = []

while True:

    number = input("Enter a number: ")

    if(number == "Done"):
        break
    
    try:
        numbers.append(int(number))
    except:
        print("Input a number!")

sum = 0

for i in range(0, len(numbers)):
    
    sum += numbers[i]


print(f"Total numbers: {len(numbers)}")
print(f"Avg: {sum / len(numbers)}\nMin: {min(numbers)}\nMax: {max(numbers)}")

numbers.sort()

print("Sorted list:", end=" ")
for i in numbers:
    print(i, end =" ")