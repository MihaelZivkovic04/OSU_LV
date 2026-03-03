
fhand = open('song.txt')

words = []
dictionary = {}

for line in fhand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        if word in dictionary.keys():
            dictionary[word] += 1
        else:
            dictionary[word] = 1

num = 0
totalNum = 0

for key in dictionary.keys():
    print(f"{key}: {dictionary[key]}")

    if(dictionary[key] == 2):
        num += 1
        totalNum += dictionary[key] 

print(f"Two times mentioned: {num} {totalNum}")

fhand.close()