hamCounter = 0
spamCounter = 0
hamWords = 0
spamWords = 0
spamExclam = 0

smsFile = open("SMSSpamCollection.txt")

for line in smsFile:
    line = line.rstrip()
    words = line.split(" ")
    if words[0].__contains__("ham"):
        hamCounter += 1
        hamWords += len(words)
    else:
        spamCounter += 1
        spamWords += len(words)
        if words[-1].endswith("!"):
            spamExclam += 1

print(words)
print("Hams = ", hamCounter, ", Spams = ", spamCounter)
print("Average number of words in hams = ", hamWords/hamCounter)
print("Average number of words in spams = ", spamWords/spamCounter)
print("Spam messages ending with ! = ", spamExclam)



        