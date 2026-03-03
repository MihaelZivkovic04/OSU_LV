
try:
    workingHours = int(input("Working hours: "))
except:
    print("Input a number!")
try:
    workingPay = float(input("Your pay per hour: "))
except:
    print("Input a number!")
print(f"Total payment: {workingHours * workingPay} EUR")