
while True:
    try:
        number = float(input("Enter a number in interval [0, 1]: "))
    except:
        print("You did not input a number!")
    if(number >= 0 and number <= 1):
        break
    else:
        print("Your number is out of the required interval!")

if(number >= 0.9):
    print("A")
elif(number >= 0.8):
    print("B")
elif(number >= 0.7):
    print("C")
elif(number >= 0.6):
    print("D")
else:
    print("F")