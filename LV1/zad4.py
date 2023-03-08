wordsDictionary = {}
counter = 0
file = open('song.txt')
for line in file:
    line = line.rstrip()
    line = line.lower()
    words = line.split(" ")
    for word in words:
        if word in wordsDictionary:
            wordsDictionary[word] += 1
        else: 
            wordsDictionary[word] = 1

for word in wordsDictionary:
    if wordsDictionary[word] == 1:
        print(word)
        counter += 1

print("There are ", counter, "words in the file that appear only once.")
