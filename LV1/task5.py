
fhand = open('SMSSpamCollection.txt')

totalHam = 0
totalSpam = 0
spam = 0
spamExclamation = 0
ham = 0

startingWithG = 0

words = []

for line in fhand:
    line = line.rstrip()
    words = line.split()

    if(words[1][0] == 'G'):
        startingWithG += 1

    if(words[0] == "ham"):
        ham += len(words) - 1
        totalHam += 1
    elif(words[0] == "spam"):
        spam += len(words) - 1
        totalSpam += 1
        if(words[-1][-1] == '!'):
            spamExclamation += 1 

print(f"Ham: {ham / totalHam}")
print(f"Spam: {spam / totalSpam}")
print(f"Spam with !: {spamExclamation}")
print(f"Starting with G: {startingWithG}")